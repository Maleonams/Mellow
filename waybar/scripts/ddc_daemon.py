#!/usr/bin/env python3
import subprocess
import time
import os
import threading

BUS = "12"
STATE = os.path.expanduser("~/.cache/ddc_brightness")
FIFO  = os.path.expanduser("~/.cache/ddc_fifo")

os.makedirs(os.path.dirname(STATE), exist_ok=True)

def get_initial():
    out = subprocess.check_output(
        ["ddcutil", "-b", BUS, "getvcp", "10", "--terse"],
        text=True
    )
    return int(out.split()[3])

brightness = get_initial()
with open(STATE, "w") as f:
    f.write(str(brightness))

lock = threading.Lock()
last_change = time.time()

def worker():
    global last_change, brightness
    while True:
        time.sleep(5)
        with lock:
            elapsed = time.time() - last_change
            value = brightness
        # applique SEULEMENT si stable depuis 200 ms
        if elapsed > 0.2:
            subprocess.Popen(
                ["ddcutil", "-b", BUS, "setvcp", "10", str(value)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            # attend un peu pour éviter le spam
            time.sleep(0.3)

threading.Thread(target=worker, daemon=True).start()

if not os.path.exists(FIFO):
    os.mkfifo(FIFO)

while True:
    with open(FIFO) as fifo:
        cmd = fifo.read().strip()
        with lock:
            if cmd == "up":
                brightness = min(brightness + 5, 100)
            elif cmd == "down":
                brightness = max(brightness - 5, 10)

            last_change = time.time()

            with open(STATE, "w") as f:
                f.write(str(brightness))

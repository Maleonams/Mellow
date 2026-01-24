#!/usr/bin/env bash
FIFO="$HOME/.cache/ddc_fifo"
STATE="$HOME/.cache/ddc_brightness"

case "$1" in
  up)   echo up   > "$FIFO" ;;
  down) echo down > "$FIFO" ;;
  get)  cat "$STATE" ;;
esac
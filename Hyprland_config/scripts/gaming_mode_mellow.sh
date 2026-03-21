notify-send "Entering gaming mode..."
sleep 2

hyprctl keyword general:border_size 1
notify-send "Reducing border size..."
hyprctl keyword general:gaps_in 0
hyprctl keyword general:gaps_out 0
notify-send "Reducing gaps sizes..."
hyprctl keyword decoration:rounding 0
hyprctl keyword decoration:rounding_power 0
notify-send "Disabling rounded corners..."
hyprctl keyword decoration:active_opacity 1
hyprctl keyword decoration:inactive_opacity 1
hyprctl keyword decoration:fullscreen_opacity 1
notify-send "Maxing out the opacity..."
hyprctl keyword decoration:blur:enabled false
notify-send "Disabling blur..."
hyprctl keyword decoration:shadow:enabled false
notify-send "Disabling shadows..."
hyprctl keyword animations:enabled false
notify-send "Disabling animations..."
pkill waybar
notify-send "killing (almost) useless pretty stuff.."
sleep 1
notify-send "Done! Gaming mode activated..."
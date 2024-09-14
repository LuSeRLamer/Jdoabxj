#!/bin/bash

# Define the script name
SCRIPT_NAME="ShishTGbot.py"

# Get the current hour
current_hour=$(date +%H)

# Run the script every hour that has passed
while true; do
  sleep $(( 3600 - $(date +%s) % 3600 ))
  echo "Restarting script at $current_hour:00"
  exec $SCRIPT_NAME
done

#!/bin/bash

# Wait for Bluetooth service to start
sleep 10

# Run the command until it succeeds
while true; do
  /home/feketej/wasp-os/tools/wasptool --device D3:7D:50:55:E4:90 --exec /home/feketej/hackarim/notification.py
  return_code=$?
  if [ $return_code -eq 0 ]; then
    break  # Exit the loop if the command succeeds
  fi
  sleep 1  # Wait for 1 second before retrying
done


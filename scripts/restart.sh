#!/bin/bash

# Get the directory of the current script
SCRIPT_DIR="$(dirname "$0")"

# Call the shutdown script
"$SCRIPT_DIR/shutdown.sh"

# Check if shutdown was successful
if [ $? -ne 0 ]; then
  echo "Failed to shut down the Docker Compose project."
  exit 1
fi

# Call the deploy script
"$SCRIPT_DIR/deploy.sh"

# Check if deploy was successful
if [ $? -eq 0 ]; then
  echo "Docker Compose project restarted successfully."
else
  echo "Failed to restart the Docker Compose project."
  exit 1
fi

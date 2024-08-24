#!/bin/bash

# Navigate to the parent directory of the script location
cd "$(dirname "$0")/.."

# Shut down the Docker Compose project
docker compose down

# Check if the Docker Compose command was successful
if [ $? -eq 0 ]; then
  echo "Docker Compose project shut down successfully."
else
  echo "Failed to shut down Docker Compose project."
fi


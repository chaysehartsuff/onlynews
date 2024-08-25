#!/bin/bash

# Navigate to the parent directory of the script location
cd "$(dirname "$0")/.."

# Copy the .env file from the current directory to the ./src/ directory
cp ./.env ./src/

# Pull down any changes and rebuild the containers if necessary
docker compose up --build -d

# Check if the Docker Compose command was successful
if [ $? -eq 0 ]; then
  echo "Docker Compose project started successfully."
else
  echo "Failed to start Docker Compose project."
  exit 1
fi

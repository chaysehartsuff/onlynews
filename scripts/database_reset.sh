#!/bin/bash

# Define the MySQL data directory
MYSQL_DATA_DIR="./mysql_data"

# Prompt the user for confirmation
read -p "This will delete all MySQL data and reset the database. Are you sure you want to continue? (y/N): " confirm

# Check if the user input is 'y' or 'Y'
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Operation canceled. No data has been deleted."
    exit 0
fi

# Stop and remove all containers and volumes associated with the Docker Compose project
docker-compose down -v

# Remove the MySQL data directory
rm -rf $MYSQL_DATA_DIR

# Recreate the MySQL data directory (optional, MySQL can create it automatically)
mkdir -p $MYSQL_DATA_DIR

# Bring up the containers again, forcing a reinitialization of the database
docker-compose up --build -d

echo "MySQL data has been reset. The database will be re-initialized on startup."

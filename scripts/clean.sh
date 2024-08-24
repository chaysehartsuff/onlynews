#!/bin/bash

# Function to remove a specific container
remove_container() {
  local container_name=$1
  docker rm -f "$container_name"
  if [ $? -eq 0 ]; then
    echo "Successfully removed container: $container_name"
  else
    echo "Failed to remove container: $container_name"
  fi
}

# Function to remove all containers
remove_all_containers() {
  # Get a list of all container IDs
  containers=$(docker ps -aq)
  
  if [ -z "$containers" ]; then
    echo "No containers to remove."
    return
  fi
  
  # Remove all containers
  docker rm -f $containers
  if [ $? -eq 0 ]; then
    echo "Successfully removed all containers."
  else
    echo "Failed to remove all containers."
  fi
}

# Check if a container name is provided
if [ -z "$1" ]; then
  echo "No container specified, purging all containers..."
  remove_all_containers
else
  echo "Purging container: $1"
  remove_container "$1"
fi

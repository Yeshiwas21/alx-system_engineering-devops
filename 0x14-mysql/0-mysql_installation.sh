#!/usr/bin/env bash
# Install MySQL on web servers

# Update and upgrade system packages
sudo apt-get update
sudo apt-get upgrade -y

# Install MySQL server (8.0.x)
sudo apt-get install -y mysql-server

# Check MySQL version
mysql --version


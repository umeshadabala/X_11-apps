#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install Xorg, Openbox (minimal window manager), xterm, xauth, and openssh-server
echo "Installing Xorg, Openbox, Xterm, Xauth, and OpenSSH Server..."
sudo apt-get install -y xorg openbox xterm xauth openssh-server

# Edit the sshd_config file to enable X11 forwarding
echo "Configuring SSH for X11 forwarding..."
sudo sed -i 's/#X11Forwarding no/X11Forwarding yes/g' /etc/ssh/sshd_config
sudo sed -i 's/#X11DisplayOffset 0/X11DisplayOffset 0/g' /etc/ssh/sshd_config
sudo sed -i 's/#X11UseLocalhost yes/X11UseLocalhost yes/g' /etc/ssh/sshd_config

# Restart SSH service to apply changes
echo "Restarting SSH service..."
sudo system restart ssh

# Start the X server (startx) and run the Python GUI app
echo "Starting the X server..."
startx &

# Give some time for the X server to start
sleep 5

# SSH to localhost with X11 forwarding and run the Python GUI app
echo "Running Python GUI application with X11 forwarding..."
ssh -X $USER@localhost "python3 main.py"


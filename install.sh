#!/bin/bash

# Function to check if a package is installed
check_package() {
    dpkg -l | grep -q "$1"
}

# Install Xorg (X11 server) if not installed
if ! check_package "xorg"; then
    echo "Installing Xorg (X11 server)..."
    sudo apt-get update
    sudo apt-get install -y xorg
fi

# Install a minimal window manager (openbox) if not installed
if ! check_package "openbox"; then
    echo "Installing Openbox (window manager)..."
    sudo apt-get install -y openbox
fi

# Install Python if not installed
if ! check_package "python3"; then
    echo "Installing Python3..."
    sudo apt-get install -y python3
fi

# Install Tkinter if not installed (for Python3)
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "Installing Tkinter for Python3..."
    sudo apt-get install -y python3-tk
fi

# Start the X server
echo "Starting X server..."
startx &

# Wait for the X server to start
while ! xdpyinfo >/dev/null 2>&1; do
    echo "Waiting for X server to start..."
    sleep 1
done

# Set the DISPLAY variable
export DISPLAY=:0

# Run the Python GUI application
echo "Running your Python GUI app..."
python3 main.py

# Optionally, stop the X server when the app closes
echo "Stopping X server..."
killall Xorg

#!/bin/bash

# List of required apt packages
apt_packages=("aircrack-ng" "wireless-tools" "iw" "net-tools" "python3" "sudo")

# Update package list
echo "Updating package list..."
sudo apt update

# Check and install each apt package
for package in "${apt_packages[@]}"; do
    if dpkg -s "$package" &> /dev/null; then
        echo "$package is already installed."
    else
        echo "$package is not installed. Installing $package..."
        sudo apt install -y "$package"
        if [ $? -eq 0 ]; then
            echo "$package installed successfully."
        else
            echo "Failed to install $package. Please check your internet connection or package sources."
            exit 1
        fi
    fi
done

# Check if pip is installed, if not install it
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt install -y python3-pip
fi

# Check and install climanu Python package
if ! python3 -m pip show climanu &> /dev/null; then
    echo "climanu is not installed. Installing climanu..."
    python3 -m pip install climanu
    if [ $? -eq 0 ]; then
        echo "climanu installed successfully."
    else
        echo "Failed to install climanu. Please check your internet connection or pip configuration."
        exit 1
    fi
else
    echo "climanu is already installed."
fi

echo "All required packages are installed."


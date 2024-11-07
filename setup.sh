#!/bin/bash

# Define the required packages for installation
apt_packages=("aircrack-ng" "wireless-tools" "iw" "net-tools" "python3" "sudo")
dnf_packages=("aircrack-ng" "wireless-tools" "iw" "net-tools" "python3" "sudo")
yum_packages=("epel-release" "aircrack-ng" "wireless-tools" "iw" "net-tools" "python3" "sudo")
pacman_packages=("aircrack-ng" "wireless_tools" "iw" "net-tools" "python" "sudo")

# Determine the package manager
if command -v apt &> /dev/null; then
    pkg_manager="apt"
    packages=("${apt_packages[@]}")
elif command -v dnf &> /dev/null; then
    pkg_manager="dnf"
    packages=("${dnf_packages[@]}")
elif command -v yum &> /dev/null; then
    pkg_manager="yum"
    packages=("${yum_packages[@]}")
elif command -v pacman &> /dev/null; then
    pkg_manager="pacman"
    packages=("${pacman_packages[@]}")
else
    echo "Unsupported Linux distribution. This script supports apt, dnf, yum, and pacman package managers."
    exit 1
fi

# Update package list if required by the package manager
echo "Updating package list..."
if [ "$pkg_manager" == "apt" ]; then
    sudo apt update
elif [ "$pkg_manager" == "dnf" ]; then
    sudo dnf check-update
elif [ "$pkg_manager" == "yum" ]; then
    sudo yum update -y
elif [ "$pkg_manager" == "pacman" ]; then
    sudo pacman -Sy
fi

# Install each required package
for package in "${packages[@]}"; do
    if ! command -v "$package" &> /dev/null; then
        echo "$package is not installed. Installing $package..."
        if [ "$pkg_manager" == "apt" ]; then
            sudo apt install -y "$package"
        elif [ "$pkg_manager" == "dnf" ]; then
            sudo dnf install -y "$package"
        elif [ "$pkg_manager" == "yum" ]; then
            sudo yum install -y "$package"
        elif [ "$pkg_manager" == "pacman" ]; then
            sudo pacman -S --noconfirm "$package"
        fi

        if [ $? -eq 0 ]; then
            echo "$package installed successfully."
        else
            echo "Failed to install $package. Please check your internet connection or package sources."
            exit 1
        fi
    else
        echo "$package is already installed."
    fi
done

# Check if pip is installed; if not, install it
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    if [ "$pkg_manager" == "apt" ]; then
        sudo apt install -y python3-pip
    elif [ "$pkg_manager" == "dnf" ]; then
        sudo dnf install -y python3-pip
    elif [ "$pkg_manager" == "yum" ]; then
        sudo yum install -y python3-pip
    elif [ "$pkg_manager" == "pacman" ]; then
        sudo pacman -S --noconfirm python-pip
    fi
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


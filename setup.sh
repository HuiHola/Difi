#!/bin/bash

# Define color codes
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"
NC="\e[0m" # No Color

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
    echo -e "${RED}Unsupported Linux distribution. This script supports apt, dnf, yum, and pacman package managers.${NC}"
    exit 1
fi

# Update package list if required by the package manager
echo -e "${YELLOW}Updating package list...${NC}"
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
        echo -e "${YELLOW}$package is not installed. Installing $package...${NC}"
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
            echo -e "${GREEN}$package installed successfully.${NC}"
        else
            echo -e "${RED}Failed to install $package. Please check your internet connection or package sources.${NC}"
            exit 1
        fi
    else
        echo -e "${GREEN}$package is already installed.${NC}"
    fi
done

# Check if pip is installed; if not, install it
if ! command -v pip3 &> /dev/null; then
    echo -e "${YELLOW}pip3 is not installed. Installing pip3...${NC}"
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

# Function to install Python packages if not already installed
install_python_package() {
    package_name=$1
    echo -e "${YELLOW}Checking if $package_name is installed...${NC}"
    if ! python3 -m pip show "$package_name" &> /dev/null; then
        echo -e "${YELLOW}$package_name is not installed. Installing $package_name...${NC}"
        python3 -m pip install "$package_name"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}$package_name installed successfully.${NC}"
        else
            echo -e "${RED}Failed to install $package_name. Please check your internet connection or pip configuration.${NC}"
            exit 1
        fi
    else
        echo -e "${GREEN}$package_name is already installed.${NC}"
    fi
}

# Install required Python packages
python_packages=("climanu" "pywifi" "mac-vendor-lookup" "rich" "ping3")
for python_package in "${python_packages[@]}"; do
    install_python_package "$python_package"
done

echo -e "${GREEN}All required packages are installed successfully.${NC}"


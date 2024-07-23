#!/bin/bash

# Define the topic and selections
TOPIC="SIMPLE_NMAP"
SELECTIONS=("Ping Scan" "Port Scan" "Service and Version Detection" "OS Detection" "Host Discovery" "Aggressive Scan" "Exit")

# Function to center text
center_text() {
    local text="$1"
    local width=$(tput cols)
    while IFS= read -r line; do
        printf "%*s\n" $(((${#line} + width) / 2)) "$line"
    done <<< "$text"
}

# Function to display the menu
display_menu() {
    clear
    center_text "=================================="

    # Display big blue "NMAP" using figlet and ANSI escape codes for blue color
    figlet_text=$(figlet "$TOPIC")
    echo -e "\e[34m$(center_text "$figlet_text")\e[0m"

    # Check and display the OS version
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        os_version="$PRETTY_NAME"
    elif command -v lsb_release &> /dev/null; then
        os_version=$(lsb_release -ds)
    else
        os_version=$(uname -s)
    fi
    center_text "OS Version: $os_version"

    # Check if Nmap is installed and display the version
    if command -v nmap &> /dev/null; then
        nmap_version=$(nmap --version | head -n 1)
        center_text "Nmap Version: $nmap_version"
    else
        center_text "Nmap is not installed."
        center_text "Press 'I' to install Nmap."
    fi

    center_text "=================================="
    for i in "${!SELECTIONS[@]}"; do
        if [ $i -eq $CURRENT_SELECTION ]; then
            center_text "-> ${SELECTIONS[i]}"
        else
            center_text "   ${SELECTIONS[i]}"
        fi
    done
    center_text "=================================="
}

# Function to install Nmap
install_nmap() {
    center_text "Installing Nmap..."
    if [ -f /etc/debian_version ]; then
        sudo apt update && sudo apt install -y nmap
    elif [ -f /etc/redhat-release ]; then
        sudo yum install -y nmap
    else
        center_text "Unsupported OS for automatic installation."
    fi
    read -p "Press any key to continue..."
}

# Initialize the current selection index
CURRENT_SELECTION=0

# Display the menu and prompt for user input
while true; do
    display_menu
    read -rsn1 input
    case "$input" in
        $'\x1b') # Handle escape sequences
            read -rsn2 -t 0.1 input
            case "$input" in
                '[A') # Up arrow
                    ((CURRENT_SELECTION--))
                    if [ $CURRENT_SELECTION -lt 0 ]; then
                        CURRENT_SELECTION=$((${#SELECTIONS[@]}-1))
                    fi
                    ;;
                '[B') # Down arrow
                    ((CURRENT_SELECTION++))
                    if [ $CURRENT_SELECTION -ge ${#SELECTIONS[@]} ]; then
                        CURRENT_SELECTION=0
                    fi
                    ;;
            esac
            ;;
        "i"|"I") # Install Nmap
            install_nmap
            ;;
        "") # Enter key
            case $CURRENT_SELECTION in
                0) python3 ping_scan.py ;;
                1) python3 port_scan.py ;;
                2) python3 service_version_detection.py ;;
                3) python3 os_detection.py ;;
                4) python3 host_discovery.py ;;
                5) python3 aggressive_scan.py ;;
                6) exit 0 ;;
                *) echo "Invalid selection" ;;
            esac
            ;;
    esac
done

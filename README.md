Simple NMAP

![image](https://github.com/user-attachments/assets/efe11d2f-d8ec-44d7-b613-94b254bceee6)

Description

This project provides a command-line interface to perform various Nmap scans using a menu-driven approach. The menu allows users to select different types of scans and handle the results, including saving them in different formats. The project includes a main script (menu.sh) that acts as a launcher for different scan types implemented in separate Python scripts.
Features

    Ping Scan: Discovers which hosts are up on a network.
    Port Scan: Scans specified ports on a target.
    Service and Version Detection: Identifies services running on open ports and their versions.
    OS Detection: Tries to determine the operating system of the target.
    Host Discovery: Discovers hosts on a network without scanning ports.
    Aggressive Scan: Combines OS detection, version detection, script scanning, and traceroute.

Requirements

    Nmap: Network scanning tool.
    Python 3: Required for running Python scripts.
    figlet: For generating large text.


    Here's a sample README.md file with instructions and descriptions for your project. You can adjust the content based on your specific setup and requirements.
Nmap Scanner Menu
Description

This project provides a command-line interface to perform various Nmap scans using a menu-driven approach. The menu allows users to select different types of scans and handle the results, including saving them in different formats. The project includes a main script (menu.sh) that acts as a launcher for different scan types implemented in separate Python scripts.
Features

    Ping Scan: Discovers which hosts are up on a network.
    Port Scan: Scans specified ports on a target.
    Service and Version Detection: Identifies services running on open ports and their versions.
    OS Detection: Tries to determine the operating system of the target.
    Host Discovery: Discovers hosts on a network without scanning ports.
    Aggressive Scan: Combines OS detection, version detection, script scanning, and traceroute.

Requirements

    Nmap: Network scanning tool.
    Python 3: Required for running Python scripts.
    figlet: For generating large text.

Installation

    Clone the Repository:

git clone <repository-url>
cd <repository-directory>

    Install Dependencies:
Make sure you have Python 3 and Nmap installed.

    Make Scripts Executable:
    
chmod +x menu.sh
chmod +x ping_scan.py
chmod +x port_scan.py
chmod +x service_version_detection.py
chmod +x os_detection.py
chmod +x host_discovery.py
chmod +x aggressive_scan.py

Enjoy

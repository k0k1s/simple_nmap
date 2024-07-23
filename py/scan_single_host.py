#!/usr/bin/env python3

import subprocess

def get_scan_type():
    scan_types = ["Single IP", "Multiple IPs", "Port Scan", "Network Discovery", "Hostname Discovery"]
    print("Select the type of scan:")
    for i, scan in enumerate(scan_types, 1):
        print(f"{i}. {scan}")
    
    choice = input("Select an option (1-5): ")
    return scan_types[int(choice) - 1]

def get_ip_address(scan_type):
    if scan_type == "Single IP":
        return input("Enter the IP address to scan: ")
    elif scan_type == "Multiple IPs":
        return input("Enter the IP addresses to scan (comma-separated): ")
    elif scan_type == "Port Scan":
        return input("Enter the IP address and port(s) to scan (e.g., 192.168.1.1 80,443): ")
    elif scan_type == "Network Discovery":
        return input("Enter the network range to scan (e.g., 192.168.1.0/24): ")
    elif scan_type == "Hostname Discovery":
        return input("Enter the hostname(s) to scan (comma-separated): ")

def perform_scan(scan_type, target):
    if scan_type == "Single IP":
        result = subprocess.run(['nmap', target], capture_output=True, text=True)
    elif scan_type == "Multiple IPs":
        ips = target.split(',')
        result = subprocess.run(['nmap'] + ips, capture_output=True, text=True)
    elif scan_type == "Port Scan":
        ip, ports = target.split()
        result = subprocess.run(['nmap', '-p', ports, ip], capture_output=True, text=True)
    elif scan_type == "Network Discovery":
        result = subprocess.run(['nmap', '-sn', target], capture_output=True, text=True)
    elif scan_type == "Hostname Discovery":
        hostnames = target.split(',')
        result = subprocess.run(['nmap'] + hostnames, capture_output=True, text=True)
    return result.stdout

def save_results(results, target):
    print("How would you like to save the results?")
    options = ["Text", "XML", "Both", "None"]
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        with open('scan_results.txt', 'w') as file:
            file.write(results)
        print("Results saved to scan_results.txt")
    elif choice == '2':
        with open('scan_results.xml', 'w') as file:
            subprocess.run(['nmap', '-oX', 'scan_results.xml', target], capture_output=True, text=True)
        print("Results saved to scan_results.xml")
    elif choice == '3':
        with open('scan_results.txt', 'w') as file:
            file.write(results)
        subprocess.run(['nmap', '-oX', 'scan_results.xml', target], capture_output=True, text=True)
        print("Results saved to scan_results.txt and scan_results.xml")
    elif choice == '4':
        print("Results not saved.")
    else:
        print("Invalid option selected.")

def main():
    scan_type = get_scan_type()
    target = get_ip_address(scan_type)
    results = perform_scan(scan_type, target)
    print(results)
    save_results(results, target)
    print("\nReturning to main menu...\n")
    subprocess.run(['./menu.sh'])

if __name__ == '__main__':
    main()

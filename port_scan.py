#!/usr/bin/env python3

import subprocess

def get_target():
    return input("Enter the IP address and ports to scan (e.g., 192.168.1.1 80,443): ")

def perform_port_scan(target):
    ip, ports = target.split()
    result = subprocess.run(['nmap', '-p', ports, ip], capture_output=True, text=True)
    return result.stdout

def main():
    target = get_target()
    results = perform_port_scan(target)
    print(results)

if __name__ == '__main__':
    main()

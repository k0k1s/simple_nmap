#!/usr/bin/env python3

import subprocess

def get_ip_range():
    return input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")

def perform_host_discovery(ip_range):
    result = subprocess.run(['nmap', '-Pn', ip_range], capture_output=True, text=True)
    return result.stdout

def main():
    ip_range = get_ip_range()
    results = perform_host_discovery(ip_range)
    print(results)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import subprocess

def get_ip_address():
    return input("Enter the IP address to scan: ")

def perform_service_version_detection(ip):
    result = subprocess.run(['nmap', '-sV', ip], capture_output=True, text=True)
    return result.stdout

def main():
    ip = get_ip_address()
    results = perform_service_version_detection(ip)
    print(results)

if __name__ == '__main__':
    main()

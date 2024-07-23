#!/usr/bin/env python3

import subprocess

def get_ip_address():
    return input("Enter the IP address to scan: ")

def perform_os_detection(ip):
    result = subprocess.run(['nmap', '-O', ip], capture_output=True, text=True)
    return result.stdout

def main():
    ip = get_ip_address()
    results = perform_os_detection(ip)
    print(results)

if __name__ == '__main__':
    main()

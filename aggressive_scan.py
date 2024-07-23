#!/usr/bin/env python3

import subprocess

def get_ip_address():
    return input("Enter the IP address to scan: ")

def perform_aggressive_scan(ip):
    result = subprocess.run(['nmap', '-A', ip], capture_output=True, text=True)
    return result.stdout

def main():
    ip = get_ip_address()
    results = perform_aggressive_scan(ip)
    print(results)

if __name__ == '__main__':
    main()

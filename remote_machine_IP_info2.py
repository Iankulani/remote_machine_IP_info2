# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:01:51 2024
@author: IAN CARTER KULANI
Email_address:iancarterkulani@gmail.com
phone number:+265(0)988061969
Purpuse: The program will prompt you to enter the remote host and then display its IP address, Afterwards it PING's IP address.
Usage: python remote_machine_IP_info.py
@author: IAN CARTER KULANI
"""
import socket
import os

def get_remote_IP_info(remote_host):
    try:
        # Get host information
        host_entry = socket.gethostbyname(remote_host)
        print(f"IP address of {remote_host}: {host_entry}")
        return host_entry
    except socket.gaierror:
        print(f"Could not resolve hostname: {remote_host}")
        return None

def ping_IP_address(ip_address):
    try:
        # Ping the IP address
        print(f"Pinging {ip_address}...")
        response = os.system(f"ping -n 4 {ip_address}")  # For Windows, use '-n 4' instead of '-c 4'
        if response == 0:
            print(f"Ping to {ip_address} was successful.")
        else:
            print(f"Ping to {ip_address} failed.")
    except Exception as e:
        print(f"An error occurred while pinging: {e}")

def main():
    remote_host = input("Enter the remote host: ")
    ip_address = get_remote_IP_info(remote_host)
    if ip_address:
        ping_IP_address(ip_address)

if __name__ == "__main__":
    main()

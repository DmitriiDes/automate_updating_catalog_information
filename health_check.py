#!/usr/bin/env python3

import psutil
import emails
import socket
import time
from ipaddress import ip_address

def check_sys_health():
    sys_health = {
               "cpu_usage" : psutil.cpu_percent(1),
               "available_disk_space" : psutil.disk_usage('/').free / psutil.disk_usage('/').total * 100,
               "available_memory" : psutil.virtual_memory().available / (1024.0 ** 2),
               "ip_localhost" : ip_address(socket.gethostbyname("localhost"))
               }
    return sys_health

def monitor_sys_health(sender, recipient):
    subject_line = ""
    email_body = "Please check your system and resolve the issue as soon as possible."
    starttime = time.time()
    sys_health = check_sys_health()
    if sys_health["cpu_usage"] > 80:
        subject_line = "Error - CPU usage is over 80%"
    if sys_health["available_disk_space"] < 20:
        subject_line = "Error - Available disk space is less than 20%"
    if sys_health["available_memory"] < 500:
        subject_line = "Error - Available memory is less than 500MB"
    if sys_health["ip_localhost"] != ip_address("127.0.0.1"):
        subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
    if subject_line:
        message = emails.generate_email(sender, recipient, subject_line, email_body)
        emails.send_email(sender, message)

def main():
    sender = "automation@example.com"
    username = input("Paste your username: ")
    recipient = username + "@example.com" #Replace username with the username given in the Connection Details Panel on the right hand side
    monitor_sys_health(sender, recipient)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import os
import shutil
import math
import sys
import socket
import psutil
def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isnt enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free= (100*du.free)/du.total
    #calculate how many free gigabytes
    gigabytes_free= du.free/math.pow(2,30)
    if gigabytes_free<min_gb or percent_free<min_percent:
        return True
    return False
def check_root_full:
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_full(disk='/', min_gb=2, min_percent=10)
def check_no_network():
    """returns True if it fails to resolve googles url, false otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return True
    except:
        return False
def check_cpu_constrained():
    """returns if the CPU is having too much usage, False otherwise """
    return psutil.cpu_percent(1)>75
def main():
    checks=[
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root pasrtition full"),
        (check_no_network, "No working network"),
        (check_cpu_constrained, "CPU load to high")
    ]
    everything_ok=True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok=False
    if not everything_ok:
        sys.exit(1)
    
    print ("Everything ok")
    sys.exit(0)

main()
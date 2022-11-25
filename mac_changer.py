#!/usr/bin/env/python



import subprocess

interface = " eth0"
new_address = "00:22:33:44:55:66"


subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig" + interface + " down ", shell=True)
subprocess.call("ifconfig" + interface + " hw ether " + new_address, shell=True)
subprocess.call("ifconfig" + interface + " up",  shell=True)

print("[+] Changing MAC address for " + interface + " to " + new_address)

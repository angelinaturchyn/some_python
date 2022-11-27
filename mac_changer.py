#!/usr/bin/env/python



import subprocess


interface = input(" interface > ")
new_address = input(" new MAC > ")


subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig" + interface + " down ", shell=True)
subprocess.call("ifconfig" + interface + " hw ether " + new_address, shell=True)
subprocess.call("ifconfig" + interface + " up",  shell=True)

print("[+] Changing MAC address for " + interface + " to " + new_address)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_address])
subprocess.call(["ifconfig", interface, "up"])

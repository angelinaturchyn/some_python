#!/usr/bin/env/python


import optparse
import subprocess

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address ")

parser.parse_args()

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

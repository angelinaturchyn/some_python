#!/usr/bin/env/python


import optparse
import subprocess

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address ")

(options, arguments) = parser.parse_args()

interface = options.interface
new_address = options.new_mac


subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig" + interface + " down ", shell=True)
subprocess.call("ifconfig" + interface + " hw ether " + new_address, shell=True)
subprocess.call("ifconfig" + interface + " up",  shell=True)

print("[+] Changing MAC address for " + interface + " to " + new_address)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_address])
subprocess.call(["ifconfig", interface, "up"])

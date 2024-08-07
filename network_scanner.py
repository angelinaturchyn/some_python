#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1)[0]

    print("IP\t\t\tMac Address\n------------------------------------------")
    for packet in answered:
     print(packet[0].psrc + "\t\t" + packet[0].hwsrc)


scan(ip)

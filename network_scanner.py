#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1)[0]

    clients_list = []
    for packet in answered:
        clients_dictionary = {"ip": packet[1].psrc, "mac_address": packet[1].hwsrc}
        clients_list.append(clients_dictionary)
    print(clients_list)

scan(ip)

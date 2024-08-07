import optparse
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for packet in answered:
        clients_dictionary = {"ip": packet[1].psrc, "mac_address": packet[1].hwsrc}
        clients_list.append(clients_dictionary)

    for client in clients_list:
        print(f"IP: {client['ip']}, MAC: {client['mac_address']}")

def main():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip_range", help="specify the IP range", metavar="IP_RANGE")
    
    (options, args) = parser.parse_args()

    if not options.ip_range:
        parser.error("IP range not given")

    scan(options.ip_range)

if __name__ == "__main__":
    main()

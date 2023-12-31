#Run from CMD for best experience!!!

import scapy.all as scapy

def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

ip_address = input("Enter the IP address or range to scan (e.g. 192.168.1.1/24): ")
results = scan_network(ip_address)

print("List of clients connected to the network:")
print("IP\t\t\tMAC Address\n-----------------------------------------")
for client in results:
    print(client["ip"] + "\t\t" + client["mac"])

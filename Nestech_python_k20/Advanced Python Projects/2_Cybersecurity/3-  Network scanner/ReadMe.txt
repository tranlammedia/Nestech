> Network Scanner
This Python script uses the Scapy library to perform a network scan
and detect which clients are connected to the network. 
The script sends an ARP request packet to a specified IP address or range, 
captures the responses, and then parses the results to extract the IP and MAC 
addresses of each client.

> Requirements
This script requires the Scapy library to be installed. You can install Scapy using pip:

pip install scapy


> Usage
To use this network scanner, simply run the script and enter 
the IP address or range to scan when prompted. 
The script will then print a list of clients connected to the network 
along with their IP and MAC addresses. The IP address or 
range should be entered in CIDR notation (e.g. 192.168.1.1/24).
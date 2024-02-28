#!/usr/bin/env python

# website_crawler.py

import requests
inport re
import urllib.parse as urlparse

target_links = []

def request(target_url):
	try:
		return requests.get(target_url)
	except requests.exceptions.ConnectionError:
		pass
		
def find_subdomains_from_wordlist(target_url):
	with open("subdomains.list", "r") as wordlist:
	
		for line in wordlist:
			test_url = line.strip() + "." + target_url
			response = request(test_url)
			
			if response:
				print("[+] Discovered subdomain --> " + test_url)	
	
def extract_links(url):
	response = request(url)
	
	if response:
		return re.findall('(?:href=")(.*?)"', response.content().decode(errors="ignore"))
	
def crawl(url):
		href_links = extract_links(url)
		
		for link in href_links:
			link = urlparse.urljoin(target_url, link)
			
			if "#" in link:
				link = link.split('#')[0]
			
			if target_url in link and link not in target_links:
				target_links.append(link)
				print(link)
				crawl(link)
		
target_url = "google.com"

find_subdomains_from_wordlist(target_url)
crawl(target_url)		

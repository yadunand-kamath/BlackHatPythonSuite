#!/usr/bin/env python

# password_hash_cracker.py

import hashlib

hash_type = str(input("Enter type of hash to be bruteforced: "))
file_path = str(input("Enter path to password wordlist: "))
decrypt_hash = str(input("Enter hash value to bruteforce: ")) 

with open(file_path, "r") as file:
	for line in file.readlines():
		if hash_type == "md5":
			hash_object = hashlib.md5(line.strip().encode())
			hashed_word = hash_object.hexdigest()
			if hashed_word == decrypt_hash:
				print("[+] Found MD5 Password --> " + line.strip())
				exit(0)
				
		if hash_type == "sha1":
			hash_object = hashlib.sha1(line.strip().encode())
			hashed_word = hash_object.hexdigest()
			if hashed_word == decrypt_hash:
				print("[+] Found MD5 Password --> " + line.strip())
				exit(0)
	
	print("[-] Password not found in wordlist")

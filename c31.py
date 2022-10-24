import subprocess
import time
import os
import urllib.request
import requests
import requests, json 

API_key = "4f1d22173f8547d7bfba4862dcec1aaa" #register for free to get it https://vpnapi.io/
server = "c2server.duckdns.org"
server_port = "4620" #this is ssh port on your server
local_server = "127.0.0.1" #this is local host from client machine
network_test = "https://twitter.com"

# 1. CHecking if client computer is connected with INternet
def connect(host=network_test):
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
	#print ("CONNECTED!!!Now proceed!!")
	#time.sleep(2)
	#print("")
	os.system('clear')
else:
	print("Hey! Connect your pc with internet! Damn!!")
	exit(1)

def checkip():
	req_amazon = requests.get('https://checkip.amazonaws.com')
	time.sleep(2)
	out = req_amazon.text
	response = requests.get("https://vpnapi.io/api/" + out + "?key=" + API_key)
	data = json.loads(response.text)
	if data["security"]["vpn"] == False:
		print("Please use VPN, your PUBLIC IP is {}".format(out))
		exit(1)
	else:
		print("Vpn detected continue!!!!...GOODLUCKY")
		time.sleep(3)
checkip();

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

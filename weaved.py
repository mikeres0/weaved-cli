import json, requests, sys, getpass, os
import api

def main():
	try:
		username = input("Enter your email address: ")
		password = getpass.getpass()
		token = api.login(username, password)
		clearScreen()
		deviceJson = api.getDevices(token)
		listDevices(deviceJson, token)
	except SyntaxError:
		print("Wrap your email address in double quotes.")
		main()

def listDevices(json, token):
	for i in json['devices']:
		print(i['devicealias'] + " || " + i['devicestate'])

	picked = int(input("Select a device: "))
	clearScreen()

	try:
		deviceAddress = json['devices'][picked]['deviceaddress']
		deviceIp = json['devices'][picked]['devicelastip']
		api.getConnectionInfo(deviceAddress, deviceIp, token)
	except:
		print("Your selection is out of range: " + str(picked) + "\n")
		listDevices(json, token)		

def clearScreen():
	if (os.name in ('ce', 'nt', 'dos')):
		os.system('cls')
	else:
		os.system('clear')

main()






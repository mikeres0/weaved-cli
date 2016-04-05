import json, requests, sys, getpass, os

def Init():
	print("+===== Weaved CLI - Mike Resoli (c) =====+")
	print("")
	print("")

	try:
		username = input("Enter your email address: ")
		password = getpass.getpass()

		url = "https://api.weaved.com/v22/api/user/login/" + username + "/" + password

		print("Connecting...")

		loginData = requests.get(url, headers={"apikey":"WeavedDemoKey$2015"}, timeout=10);

		loginJson = json.loads(loginData.text)

		if loginJson['status'] == "true":
			clearScreen()
			token = loginJson['token']
			getDevices(token)
		else:
			print("Error 1: Unable to connect to api.weaved.com. Check your credentials.")
			sys.exit()
	except SyntaxError:
		print("Wrap your email address in double quotes.")
		Init()


def getDevices(token):
	url = "https://api.weaved.com/v22/api/device/list/all"

	print("Retrieving devices using token " + token)

	deviceData = requests.get(url, headers={"apikey":"WeavedDemoKey$2015","token":token}, timeout=10);

	deviceJson = json.loads(deviceData.text)

	if deviceJson['status'] == "true":
		listDevices(deviceJson, token)
	else:
		print("Error 2: There was a problem retrieving the device list");
		sys.exit()

def listDevices(json, token):
	print("Listing devices...")
	print("")
	print("+===== Devices =====+")
	for i in json['devices']:
		print(i['devicealias'] + " || " + i['devicestate'])

	print("")

	picked = int(input("Select a device (enter 0 for the first): "))

	clearScreen()

	try:
		deviceAddress = json['devices'][picked]['deviceaddress']
		deviceIp = json['devices'][picked]['devicelastip']
		print("Getting connection info for " + json['devices'][picked]['devicealias'])
		getConnectionInfo(deviceAddress, deviceIp, token)
	except:
		print("Your selection is out of range.")
		print("")
		listDevices(json, token)


def getConnectionInfo(deviceAddress, hostIp, token):
	url = "https://api.weaved.com/v22/api/device/connect"

	connectionData = requests.post(url, headers={"apikey":"WeavedDemoKey$2015","token":token}, json={"deviceaddress":deviceAddress,"hostip":hostIp,"wait":"true"}, timeout=20);

	connectionJson = json.loads(connectionData.text)

	if connectionJson['status'] == "true":
		print("")
		print("Connection: " + connectionJson['connection']['proxy'])
	else:
		print("Error 3: There was a problem getting the connection details.")

def clearScreen():
	if (os.name in ('ce', 'nt', 'dos')):
		os.system('cls')
	else:
		os.system('clear')


Init()






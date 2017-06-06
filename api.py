import json, requests, sys

def login(username, password):
	url = "https://api.weaved.com/v22/api/user/login/" + username + "/" + password

	loginData = requests.get(url, headers={"apikey":"WeavedDemoKey$2015"}, timeout=10);

	loginJson = json.loads(loginData.text)

	if loginJson['status'] == "true":
		token = loginJson['token']
		return token
	else:
		print("Error 1: Unable to connect to api.weaved.com. Check your credentials.")
		sys.exit()

def getDevices(token):
	url = "https://api.weaved.com/v22/api/device/list/all"

	deviceData = requests.get(url, headers={"apikey":"WeavedDemoKey$2015","token":token}, timeout=10);

	deviceJson = json.loads(deviceData.text)

	if deviceJson['status'] == "true":
		return deviceJson
	else:
		print("Error 2: There was a problem retrieving the device list");
		sys.exit()


def getConnectionInfo(deviceAddress, hostIp, token):
	url = "https://api.weaved.com/v22/api/device/connect"

	connectionData = requests.post(url, headers={"apikey":"WeavedDemoKey$2015","token":token}, json={"deviceaddress":deviceAddress,"hostip":hostIp,"wait":"true"}, timeout=20);

	connectionJson = json.loads(connectionData.text)

	if connectionJson['status'] == "true":
		print("Connection: " + connectionJson['connection']['proxy'])
	else:
		print("Error 3: There was a problem getting the connection details.")
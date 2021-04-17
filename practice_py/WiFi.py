from subprocess import *

data = check_output(["netsh", "wlan", "show", "profile"]
                    ).decode("utf-8").split("\n")
wifis = [line.split(":")[1][1:-1]
         for line in data if "All User Profile" in line]

for wifi in wifis:
	r = check_output(["netsh", "wlan", "show", "profile", wifi,
                   "key=clear"]).decode("utf-8").split("\n")
	r = [line.split(":")[1][1:-1] for line in r if "Key Content" in line]
	try:
		print(f"Name: {wifi}, Password: {r[0]}")
	except IndexError:
		print(f"Name: {wifi}, Password: Can not be read!")

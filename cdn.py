import requests, json, itertools, sys, os, threading, time

try:
	asset_id = int(input("ID: "))
except:
	print("Error!")
	exit()

sf = open("scraped.jhinscripter", "a")
auth_cookie = open("auth_cookie.txt", "r").read()
if auth_cookie == "":
	print("No Auth_Cookie Detected!")
	exit()
curr_npc = [""]
finished = False
cpn = 1

def loadinganimation():
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if finished:
			break
		sys.stdout.write("\rWorking on " + c)
		sys.stdout.flush()
		time.sleep(0.3)
	os.system("cls")
	print("Done!\nAll saved into 'scraped.jhinscripter'.")
	exit()

os.system("cls")
threading.Thread(target=loadinganimation).start()

while True:
	os.system("cls")
	print(f"\nPage number: {cpn}")
	res = json.loads(requests.Session().get(f"https://inventory.roblox.com/v2/assets/{asset_id}/owners?sortOrder=Asc&limit=100&cursor={curr_npc[0]}", cookies={".ROBLOSECURITY":auth_cookie}).text)

	xxx = []

	[(xxx.append(o["owner"]["id"]) if o["owner"] else None) for o in res["data"]]
	
	for i in xxx:
		sf.write(f"{str(json.loads(requests.get(f'http://api.roblox.com/Users/{i}').text)['Username'])}\n")

	if res["nextPageCursor"]:
		curr_npc.pop(0)
		curr_npc.append(res["nextPageCursor"])
	else:
		finished = True
		exit()

	cpn += 1
import requests, json

data = {"metadata":{"uuid": "cb10023fa31833944199a8730c7c1aec", "major": 777, "minor": 777, "isEnterState": False, "isActive": True}}

## CREATE a DATA
resp = requests.post('https://api.mesosfer.com/api/v2/data/bucket/Attendance',
	 data=json.dumps(data),
     headers={'Content-Type':'application/json', 'Authorization':'Bearer ACCESS_TOKEN', 'X-Mesosfer-AppId':'APP_ID', 'X-Mesosfer-AppKey':'APP_KEY'})

print(resp.json())
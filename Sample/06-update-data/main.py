import requests

data = {"metadata":{"uuid": "cb10023fa31833944199a8730c7c1aec", "major": 888, "minor": 888, "isEnterState": True, "isActive": True}}

## UPDATE a DATA
resp = requests.put('https://api.mesosfer.com/api/v2/data/bucket/Attendance/OBJECT_ID',
	 json=data,
     headers={'Content-Type':'application/json', 'Authorization':'Bearer ACCESS_TOKEN', 'X-Mesosfer-AppId':'APP_ID', 'X-Mesosfer-AppKey':'APP_KEY'})

print(resp.json())
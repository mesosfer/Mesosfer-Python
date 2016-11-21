import requests

data = {"data":{"title": "Hi", "alert": "Thanks for coming."}}

## PUSH NOTIFICATION
resp = requests.post('https://api.mesosfer.com/api/v2/push/notification',
	 json=data,
     headers={'Content-Type':'application/json', 'Authorization':'Bearer ACCESS_TOKEN', 'X-Mesosfer-AppId':'APP_ID', 'X-Mesosfer-AppKey':'APP_KEY'})

print(resp.json())
import requests

#### LOGIN USER
data = {"email": "john.doe@gmail.com", "password": "johndoe"}

resp = requests.post('https://api.mesosfer.com/api/v2/users/signin',
	 json=data,
	 headers={'Content-Type':'application/json', 'X-Mesosfer-AppId':'APP_ID', 'X-Mesosfer-AppKey':'APP_KEY'})

print(resp.json())
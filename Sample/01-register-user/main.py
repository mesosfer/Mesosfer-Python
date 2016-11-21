import requests

#### REGISTER USER
data = {"firstname": "John", "lastname": "Doe", "email": "john.doe@gmail.com", "password": "johndoe"}

resp = requests.post('https://api.mesosfer.com/api/v2/users',
	 json=data,
	 headers={'Content-Type':'application/json', 'Authorization':'Bearer ACCESS_TOKEN', 'X-Mesosfer-AppId':'APP_ID', 'X-Mesosfer-AppKey':'APP_KEY'})

print(resp.json())
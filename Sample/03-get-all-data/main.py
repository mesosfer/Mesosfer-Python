import requests

# GET ALL DATA
resp = requests.get('https://api.mesosfer.com/api/v2/data/bucket/Attendance',
                     headers={'Content-Type':'application/json', 'Authorization':'Bearer ACCESS_TOKEN', 'X-Mesosfer-AppId':'APP_ID', 'X-Mesosfer-AppKey':'APP_KEY'})

print(resp.json())
import requests

# DELETE a DATA
resp = requests.delete('https://api.mesosfer.com/api/v2/data/bucket/Attendance/OBJECT_ID',
 	headers={'Content-Type':'application/json', 'Authorization':'Bearer ACCESS_TOKEN', 'X-Mesosfer-AppId':'APP_ID', 'X-Mesosfer-AppKey':'APP_KEY'})

print(resp.json())
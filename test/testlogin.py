import requests

payload = {'username': 'root', 'password': 'root'}

response = requests.post(
    'http://localhost:8000/api/signin',
    data=payload,
    headers={
        "content-type": "application/json"
    })
# sessionid = response.cookies['sessionid']

print(response)

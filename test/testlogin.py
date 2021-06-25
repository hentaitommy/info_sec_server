import requests

payload = {'username': 'hentaitommy', 'password': 'scut123456'}

s = requests.session() #建立一个Session
response = s.post('http://localhost:8000/api/signin', json=payload)
print(response.text)

response = s.get('http://localhost:8000/api/userinfo')
print(response.text)

response = s.get('http://localhost:8000/api/query?action=querySelf')
print(response.text)

response = s.get('http://localhost:8000/api/query?action=queryAll')
print(response.text)
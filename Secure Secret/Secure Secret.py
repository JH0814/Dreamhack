import itsdangerous
import zlib

cookie = ".eJwty7sVgCAMAMBdWIDESCBuA_nYWImdz921sLvm7jRdT7_S9mPmAYLoSgbqEYuM3pClSKlkOEhLR5LFmVEreTWwOgJhjS81Jspx9D09L-nVGrE.Z8gH9A.Usydu_PtcujoxISq6CaUfMYkmTM" 
encoded_payload = cookie.split(".")[1]  

payload = itsdangerous.base64_decode(encoded_payload)
payload = zlib.decompress(payload)

secret_path = payload.decode('utf-8')

print(secret_path)
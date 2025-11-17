from Crypto.Util.number import inverse, long_to_bytes
from pwn import *

p = remote(ADDR, PORT)
p.sendlineafter(b"[3] Get info\n", b"3")
p.recvuntil(b"N: ")
N = int(p.recvline())
p.recvuntil(b"e: ")
e = int(p.recvline())
p.recvuntil(b"FLAG: ")
enc = int(p.recvline())

S = 2
S_inv = inverse(S, N)

s_enc = pow(S, e, N)
C_prime = (enc * s_enc) % N
payload = hex(C_prime)[2:]
p.sendlineafter(b"[3] Get info\n", b"2")
p.sendlineafter(b"(hex): ", payload.encode())
s_pt = int(p.recvline())
pt = (s_pt * S_inv) % N
print("Flag : " + long_to_bytes(pt).decode())
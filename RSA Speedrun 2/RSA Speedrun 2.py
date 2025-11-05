from pwn import *
from Crypto.Util.number import *
import math

con = remote(ADDRESS, PORT)

l_d = []
l_n = []

for i in range(10):
    con.recvuntil(b"e = ")
    e = int(con.recvline())
    con.recvuntil(b"n = ")
    n = int(con.recvline())
    con.recvuntil(b"c = ")
    c = int(con.recvline())
    con.recvuntil(b"hint = ")
    h = int(con.recvline())
    p = int((h + math.isqrt(h ** 2 + 4 * n)) // 2)
    q = n // p
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    l_d.append(d)
    l_n.append(n)
    con.sendlineafter(b"> ", str(m).encode())

c = int(con.recvline())
for i in range(len(l_n)):
    m = pow(c, l_d[i], l_n[i])
    m = long_to_bytes(m)
    if m.startswith(b"DH{"):
        print("Flag : " + m.decode())
        break
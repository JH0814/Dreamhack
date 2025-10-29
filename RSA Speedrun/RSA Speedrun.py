from pwn import *
from sympy.ntheory import factorint

con = remote(ADDRESS, PORT)

for i in range(1, 11):
    con.recvuntil(b"e = ")
    e = int(con.recvline())
    con.recvuntil(b"n = ")
    n = int(con.recvline())
    con.recvuntil(b"c = ")
    c = int(con.recvline())
    factors = factorint(n)
    p, q = list(factors.keys())
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    con.sendlineafter(b"> ", str(m).encode())

con.interactive()


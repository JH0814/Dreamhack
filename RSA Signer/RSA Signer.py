from pwn import *
import math
from Crypto.Util.number import long_to_bytes

p = remote(ADDRESS, PORT)

p.recvuntil(b"N = ")
N = int(p.recvline().strip())
p.recvuntil(b"S = ")
S = int(p.recvline().strip())

p.sendlineafter(b"d_q : ", b"d_p")
p.sendlineafter(b"d_p : ", b"1")
p.recvuntil(b"your_S = ")
your_S = int(p.recvline().strip())

p.recvuntil(b"encrypt_flag = ")
encrypt_flag = int(p.recvline().strip())

q = math.gcd(S - your_S, N)
p = N // q
phi = (p - 1) * (q - 1)
d = pow(65537, -1, phi)
print(long_to_bytes(pow(encrypt_flag, d, N)).decode('ascii'))
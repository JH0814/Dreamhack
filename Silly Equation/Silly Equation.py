import struct
from pwn import *

def double_to_long_bits(d: float) -> int:
  packed = struct.pack('>d', d)
  return struct.unpack('>Q', packed)[0]

val = 0.0 + 0.1 + 0.2
long_val = double_to_long_bits(val)

#p = process("./main")
p = remote(ADDRESS, PORT)
p.sendlineafter(b" : ", str(long_val))
p.interactive()
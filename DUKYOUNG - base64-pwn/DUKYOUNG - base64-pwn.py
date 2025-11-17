import base64
from pwn import *

def rev(s):
    ans = []
    for i in range(len(s)):
        c = ord(s[i])
        c = c ^ 0x55
        c = ((c << 1) | (c >> 7)) & 0xFF
        ans.append(c)
    return ans


s = "cat flag"
ans = rev(s)
payload = base64.b64encode(bytes(ans))

#p = process("./prob")
p = remote(ADDR, PORT)
p.sendlineafter(b"? ", payload)
p.interactive()

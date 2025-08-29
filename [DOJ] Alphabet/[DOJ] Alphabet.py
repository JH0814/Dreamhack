from pwn import *

context.arch = 'amd64'

code = '''
mov rax, rdi
add rax, 64
ret
'''

shellcode = asm(code)
print(shellcode.hex())

p = remote(ADDRESS, PORT)
p.sendlineafter(b"> ", str(shellcode.hex()).encode())
p.interactive()
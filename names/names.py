from pwn import *
def sub_1349(n):
    tmp = ((18048 * n) & 0xFFFF) | (((4660 * n) & 0xFFFF) >> 11)
    result = (22136 * tmp) & 0xFFFF
    return result

def sub_138A(data, seed):
    a3 = seed
    length = len(data)
    for i in range(length // 2):
        word = int.from_bytes(data[i*2:i*2+2], 'little')
        v3 = sub_1349(word)
        temp = v3 ^ a3
        rotated = ((temp << 7) | (temp >> 9)) & 0xFFFF
        a3 = (5 * rotated - 8531) & 0xFFFF
    v8 = 0
    if length % 2 != 0:
        v8 = data[-1]
    v4 = sub_1349(v8)
    temp = (length ^ v4 ^ a3) & 0xFFFF
    v10 = ((-8531) * (((temp >> 8) ^ temp))) & 0xFFFF
    temp_final = ((-8531) * ((v10 >> 5) ^ v10)) & 0xFFFF
    final_hash = ((temp_final >> 8) ^ temp_final) & 0xFFFF
    return final_hash

for i in range(33, 127):
    for j in range(33, 127):
        for k in range(33, 127):
            cand = chr(i) + chr(j) + chr(k)
            cur = sub_138A(cand.encode('ascii'), 0xcafe)
            if cur == 0x0796:
                print("answer : ", cand)
                p = remote(ADDRESS, PORT)
                p.sendlineafter("> ", cand.encode())
                p.interactive()
                exit(0)
        
                

def calculate(a1):
    x = (a1 ^ 0x3C) & 0xFF
    r1 = ((x << 2) | (x >> 6)) & 0xFF
    r2 = (5 * r1 + 125) & 0xFF
    r3 = ((r2 >> 3) | (r2 << 5)) & 0xFF
    x2 = (r3 ^ 0xB2) & 0xFF
    r4 = ((x2 << 4) | (x2 >> 4)) & 0xFF
    v3 = (3 * r4 - 47) & 0xFF
    r5 = ((v3 << 1) | (v3 >> 7)) & 0xFF
    v4 = (r5 ^ 0xD4) & 0xFF
    v5 = 0
    temp_v4 = v4
    for _ in range(8):
        v5 = (v5 << 1) | (temp_v4 & 1)
        temp_v4 >>= 1
    return v5
table = {}
for i in range(256):
    output = calculate(i)
    table[output] = i

outputs = [151, 185, 177, 238, 202, 227, 177, 25, 101, 195, 183, 193, 227, 59, 232, 183, 185, 59, 185, 98, 232, 189, 183, 185, 101, 205, 185, 25, 193, 59, 205, 177, 183, 195, 238, 193, 195, 238, 183, 202, 232, 195, 193, 177, 59, 25, 238, 205, 232, 151, 189, 205, 101, 98, 101, 189, 177, 59, 101, 151, 238, 189, 183, 205]
flag = ""
for val in outputs:
    cc = table[val]
    flag += chr(cc)

print("Flag : " + flag)

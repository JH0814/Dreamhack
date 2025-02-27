arr = [0x52, 0xDF, 0xB3, 0x60, 0xF1, 0x8B, 0x1C, 0xB5, 0x57, 0xD1, 0x9F, 0x38, 0x4B, 0x29, 0xD9, 0x26, 0x7F, 0xC9, 0xA3, 0xE9, 0x53, 0x18, 0x4F, 0xB8, 0x6A, 0xCB, 0x87, 0x58, 0x5B, 0x39, 0x1E]

ans = []

def ror(num, cl):
    tmp1 = num >> cl
    tmp2 = num << (8 - cl)
    tmp2 &= 255
    return tmp1 | tmp2

for i in range(len(arr)):
    cl = i & 7
    res = ror(arr[i] ^ i, cl)
    ans.append(chr(res))

print(''.join(ans))
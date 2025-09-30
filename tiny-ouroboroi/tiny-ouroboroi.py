def sub_12A5_rev(b):
    return ~b & 0xFF

def sub_126C_rev(b, cnt):
    cnt %= 8
    return ((b >> cnt) | (b << (8 - cnt))) & 0xFF

with open("output.bin", "rb") as f:
    output_data = f.read()

flag = []
for i, val in enumerate(output_data):
    cur = val
    if i % 2 != 0:
        cur = sub_12A5_rev(cur)
    cur = sub_126C_rev(cur, i)
    flag.append(chr(cur))

print("Flag : ", "".join(flag))

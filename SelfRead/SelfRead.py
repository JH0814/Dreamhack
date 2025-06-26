EXECUTABLE_PATH = "./prob" 

KEY = b'\x2a\x22\xa4\x7f\x25\x11\x6b\x77\x69\xf2\x70\x6b\x7c\x69\x7c'

with open(EXECUTABLE_PATH, "rb") as f:
    f.seek(1337)
    data = f.read(1024)

indices = []
for i, byte in enumerate(data[0:], start=0):
    if byte != 0:
        indices.append(i)
    if len(indices) == 15:
        break

result_bytes = []
for i in range(15):
    decrypted_byte = data[indices[i]] ^ KEY[i]
    result_bytes.append(decrypted_byte)

for i in result_bytes:
    if i <= 128:
        print(chr(i), end='')
    else:
        print(chr(i % 128), end='')
print()
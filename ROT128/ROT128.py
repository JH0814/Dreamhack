hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]
with open('encfile', 'r', encoding='utf-8') as f:
    enc = f.read()

enc_list = [enc[i:i+2] for i in range(0, len(enc), 2)]
plain_list = list(range(len(enc_list)))

for i in range(len(enc_list)):
    hex_b = enc_list[i]
    idx = hex_list.index(hex_b)
    plain_list[i] = hex_list[(idx - 128) % 256]

plaintext = bytes([int(i, 16) for i in plain_list])

with open('flag.png', 'wb') as f:
    f.write(plaintext)


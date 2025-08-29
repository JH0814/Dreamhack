from pwn import *

state = [0] * 8
g_index = 0

def sub_1507():
    global state, g_index
    for i in range(8):
        v1 = ((state[i] & 0x8000) | (state[(i + 1) % 8] & 0x7FFF)) >> 1
        if (state[(i + 1) % 8] & 1) != 0:
            v1 ^= 0x9908
        result = (v1 ^ state[(i + 4) % 8]) & 0xFFFF
        state[i] = result
    g_index = 0

def sub_15D4():
    global state, g_index
    if g_index > 7:
        sub_1507()
    v7 = state[g_index]
    g_index += 1
    v6 = (v7 >> 12) & 0xF
    n2 = (v7 >> 8) & 0xF
    n1 = (v7 >> 4) & 0xF
    n0 = v7 & 0xF
    v1 = 5 * n1 + 3 * n0 + 7 * n2 + 2 * v6
    v2 = 6 * n2 + 7 * n1 + 4 * n0 + 3 * v6
    v4 = 5 * n0 + 6 * n1 + 4 * n2 + 7 * v6
    nibble2 = (3 * n1 + 2 * n0 + 5 * n2 + 4 * v6) & 0xF
    result = (
        ((v4 & 0xF) << 12) |
        (nibble2 << 8) |
        ((v2 & 0xF) << 4) |
        (v1 & 0xF)
    )
    return result & 0xFFFF

def sub_147B(seed):
    global state, g_index
    state = [0] * 8
    state[0] = seed & 0xFFFF
    for i in range(1, 8):
        prev = state[i - 1]
        val = 27655 * (prev ^ (prev >> 14)) + i
        state[i] = val & 0xFFFF
    g_index = 8

word_list = []
with open('dictionary.txt', 'r') as f:
    word_list = [line.strip() for line in f.readlines()]

#p = process('./chall')
p = remote("host8.dreamhack.games", 13154)
easy_word = []
for i in range(10):
    p.recvuntil(b"Type this word as soon as possible: ")
    word = p.recvline().strip()
    easy_word.append(word)
    p.sendlineafter(b"> ", word)

found_seed = -1
for s in range(65536):
    sub_147B(s)
    generated_words = []
    for _ in range(10):
        rand_val = sub_15D4()
        word_index = rand_val % len(word_list) 
        generated_words.append(word_list[word_index].encode())
    if generated_words == easy_word:
        found_seed = s
        break

if found_seed == -1:
    print("Not found")
    exit()

print("Predicting HARD MODE words")
sub_147B(found_seed)
for _ in range(10):
    sub_15D4()

hard_words = []
for _ in range(10):
    rand_val = sub_15D4()
    word_index = rand_val % len(word_list)
    hard_words.append(word_list[word_index].encode())

print("Starting HARD MODE")
for word in hard_words:
    p.recvuntil(b"[REDACTED]")
    p.sendlineafter(b"> ", word)

print("HARD MODE Cleared!")
p.interactive()
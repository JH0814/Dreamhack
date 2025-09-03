from pwn import *
from z3 import *

class CustomRandom2048:
    def __init__(self, seed):
        mask = (1 << 64) - 1
        self.state = []
        for i in range(32):
            s = (seed >> (64 * (31-i))) & mask
            self.state.append(s)
        self.p = 0

    def next(self):
        mask = (1 << 64) - 1
        s0 = self.state[self.p]
        s1 = self.state[(self.p+1) % 32]
        out = (s0 ^ ((s1 << 13) & mask)) & mask
        self.state[self.p] = ((s0 + s1 + 0xCAFEBABE12345678) ^ 0x1337DEADBEEF) & mask
        self.p = (self.p + 1) % 32
        return out

    def getrandbits(self, nbits=2048):
        output = 0
        for _ in range(nbits // 64):
            output = (output << 64) | self.next()
        return output


p = remote(ADDRESS, PORT)
p.recvuntil(b"You are session #")
session_id = int(p.recvline()[:-1])
p.sendafter(b"number: ", b"giveup")
p.recvuntil(b"The answer was:\n")
answer_0 = p.recvline()[:-1]
print(answer_0)
p.close()

answer_0 = int(answer_0.decode())
MASK = (1 << 64) - 1
solver = Solver()
s = [BitVec(f's_{i}', 64) for i in range(32)]
outs = []
temp_answer = answer_0
for _ in range(32):
    outs.insert(0, temp_answer & MASK)
    temp_answer >>= 64

current_state = s[:]
for i in range(32):
    p_val = i
    s0 = current_state[p_val]
    s1 = current_state[(p_val + 1) % 32]
    constraint = (outs[i] == (s0 ^ (s1 << 13)))
    solver.add(constraint)
    updated_s0 = ((s0 + s1 + 0xCAFEBABE12345678) ^ 0x1337DEADBEEF)
    current_state[p_val] = updated_s0

if solver.check() == sat:
    model = solver.model()
    recovered_state = [model[var].as_long() for var in s]
    seed_0 = 0
    for val in recovered_state:
        seed_0 = (seed_0 << 64) | val
else:
    print("[-] Z3가 해를 찾지 못했습니다. 프로그램을 종료합니다.")
    exit()

init_seed = seed_0 - session_id
print(f"[+] 서버의 INIT_SEED 계산 완료")
print("[+] 플래그를 획득하기 위해 서버에 다시 연결합니다")
p2 = remote(ADDRESS, PORT)
p2.recvuntil(b"You are session #")
next_session_id = int(p2.recvline()[:-1])
print(f"[+] 두 번째 세션 ID: {next_session_id}")
predicted_seed = init_seed + next_session_id
local_rng = CustomRandom2048(predicted_seed)
predicted_answer = local_rng.getrandbits(2048)
print(f"[+] 정답 예측 완료")

p2.sendlineafter(b"number: ", str(predicted_answer).encode())

response = p2.recvall(timeout=2)
print("-------- 최종 서버 응답 ---------")
print(response.decode())
print("--------------------------")
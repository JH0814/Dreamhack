import itertools
import string

def solve():
    with open("flag.txt.enc", "rb") as f:
        enc_data = f.read()
    known_plain = b'DH{'
    key_part = [p ^ e for p, e in zip(known_plain, enc_data)]
    if not (key_part[0] // 8 == key_part[1] // 8 == key_part[2] // 8):
        print("오류: 키 구조가 예상과 다릅니다.")
        return
    h0 = key_part[0] // 8
    m_parts = [k % 8 for k in key_part]
    if len(set(m_parts)) != 3:
        print("오류: M 값에 중복이 있어 순열이 아닙니다.")
        return
    m0, m1, m2 = m_parts[0], m_parts[1], m_parts[2]
    h_rest = [i for i in range(8) if i != h0]
    m_rest = [i for i in range(8) if i not in m_parts]
    for h_perm in itertools.permutations(h_rest):
        H = [h0] + list(h_perm)
        for m_perm in itertools.permutations(m_rest):
            M = [m0, m1, m2] + list(m_perm)
            keystream = []
            for h_val in H:
                for m_val in M:
                    keystream.append(8 * h_val + m_val)
            dec_data = bytes([e ^ k for e, k in zip(enc_data, keystream)])
            valid_chars = (string.ascii_letters + "_").encode('ascii')
            body = dec_data[3:63]
            if (dec_data.startswith(b'DH{') and 
                dec_data.endswith(b'}') and
                all(c in valid_chars for c in body)):
                print("Flag : ")
                print(dec_data.decode('ascii'))
                return
    print("Can't find flag")

if __name__ == "__main__":
    solve()
from pwn import *

p = process('./queen')
#p = remote(ADDRESS, PORT)

def is_safe(row, col, queens): # 안전한 위치인지 확인하는 함수
        for r, c in queens.items():
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

def backtrack(k, row_list, answer, given_queens): # 탐색을 진행하는 함수
        if k == len(row_list):
            return True

        cur_row = row_list[k]
        for col in range(16):
            if is_safe(cur_row, col, given_queens) and is_safe(cur_row, col, answer):
                answer[cur_row] = col 
                if backtrack(k + 1, row_list, answer, given_queens):
                    return True
                del answer[cur_row]
        return False


def solve_queens(given_queens): # 16-queen 전체 solve 함수
    left_rows = [r for r in range(16) if r not in given_queens]
    answer = {}

    if backtrack(0, left_rows, answer, given_queens):
        return answer
    else:
        return None

p.recvuntil(b"I will give you a flag.\n")

for i in range(100):
    p.recvuntil(b"Queen -> ")
    line = p.recvline().decode()
    coords = []
    cleaned_line = line.strip().replace('(', '').replace(')', '')
    numbers = cleaned_line.split(',')
    for i in range(0, len(numbers), 2):
        row_str = numbers[i]
        col_str = numbers[i+1]
        coords.append((row_str.strip(), col_str.strip()))
    given_queens = {int(r): int(c) for r, c in coords}
    answer = solve_queens(given_queens)
    
    if answer is None:
        log.error("Failed to find a solution!")
        break
    
    p.recvuntil(b"Place the remaining queens!\n")

    for r, c in answer.items():
        payload = f"{r} {c}".encode()
        p.sendline(payload)
    
    result = p.recvline().strip()
    if b"Good Job!" in result:
        log.success("Round completed successfully!")
    else:
        log.error(f"Round failed. Response: {result.decode()}")
        break
flag = p.recvall(timeout=2).decode(errors='ignore').strip()
log.success(f"FLAG: {flag}")

p.close()
from pwn import *

#p = process("./knight")
p = remote(ADDRESS, PORT)

initial_state = b"B***...WBW.*..**"
target_state  = b"W***...BWB.*..**"

knight_moves = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

def state_to_board(state):
    return [list(state[i:i+4]) for i in range(0, 16, 4)]

def board_to_state(board):
    return b"".join(bytes([c]) for row in board for c in row)

def get_moves(state):
    moves = []
    board = state_to_board(state)
    for r in range(4):
        for c in range(4):
            if board[r][c] in [ord('B'), ord('W')]:
                for dr, dc in knight_moves:
                    nr = r + dr 
                    nc = c + dc
                    if 0 <= nr < 4 and 0 <= nc < 4 and board[nr][nc] == ord('.'):
                        new_board = [row[:] for row in board]
                        new_board[nr][nc] = new_board[r][c]
                        new_board[r][c] = ord('.')
                        
                        move_info = (r, c, nr, nc)
                        moves.append((board_to_state(new_board), move_info))
    return moves

def BFS():
    queue = [(initial_state, [])]
    visited = {initial_state}
    while queue:
        cur, path = queue.pop(0)
        if cur == target_state:
            print("Solution Found!!")
            return path
        for next, move in get_moves(cur):
            if next in visited:
                continue
            else:
                visited.add(next)
                new_path = path + [move]
                queue.append((next, new_path))
    print("Failed")
    return None

solution = BFS()
if solution:
    for i in range(40):
        p.recvuntil(b" : ")
        if i < len(solution):
            move = solution[i]
            move_str = f"{move[0]} {move[1]} {move[2]} {move[3]}".encode()
            p.sendline(move_str)
        else:
            move = solution[-1]
            move_str = f"{move[0]} {move[1]} {move[2]} {move[3]}".encode()
            p.sendline(move_str)
    p.interactive()
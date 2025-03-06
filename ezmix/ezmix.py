def sub_12C2(k, val):
    return ((k >> (val & 7)) | (k << (8 - (val & 7)))) & 0xFF

with open("program.bin", "rb") as f:
    command_byte = f.read()
with open("output.bin", "rb") as f:
    answer_byte = f.read()

command = []
answer = []

for i in range(len(command_byte)):
    command.append(command_byte[i])
for i in range(len(answer_byte)):
    answer.append(answer_byte[i])


for i in range(len(command) - 2, -1, -2):
    com = command[i]
    val = command[i + 1]
    if com == 1:
        for j in range(len(answer)):
            answer[j] = (answer[j] - val) & 0xFF
    elif com == 2:
        for j in range(len(answer)):
            answer[j] = (val ^ answer[j]) & 0xFF
    elif com == 3:
        for j in range(len(answer)):
            for k in range(256):
                if sub_12C2(k, val) == answer[j]:
                    answer[j] = k
                    break

for i in range(len(answer)):
    print(chr(answer[i]), end='')
print()
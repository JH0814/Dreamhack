import io

def decode(a1,a2):
    prev = -1
    while True :
        c = a1.read(1)
        if not c :
            break
        a2.write(c)
        if prev == c :
            while True :
                c = a1.read(1)
                if not c :
                    break
                if c != prev :
                    change = int.from_bytes(c,byteorder='little')
                    for i in range(change) :
                        a2.write(prev)
                    break
        else:
            prev = c

with open('secretMessage.enc','rb') as a1, open('secretMessage.raw','wb') as a2:
    decode(a1, a2)
plain = "EDVLF FUBSWR GUHDPKDFN"

for j in range(26):
    ans = ""
    for i in range(len(plain)):
        if plain[i] != " ":
            ans += chr((ord(plain[i]) + j - ord('A')) % 26 + ord('A'))
        else:
            ans += "_"
    print(f"{j} case : {ans}")
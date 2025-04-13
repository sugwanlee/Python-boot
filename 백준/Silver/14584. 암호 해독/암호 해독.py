code = input()
words = [input() for i in range(int(input()))]

def decode(c):
    dec = []
    for i in c:
        a = ord(i) + 1
        if a == 123:
            a = 97
        dec.append(chr(a))
    return "".join(dec)

b = ""
for word in words:
    for i in range(1,27): 
        word = decode(word)
        if word in code:
            dec = []
            for j in code:
                a = ord(j) - i
                if a < 97:
                    a = a + 26
                dec.append(chr(a))
            b = "".join(dec)
            break
    if b:
        break
print(b)

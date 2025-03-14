def solution(s):
    a = [0,0]
    while s != "1":
        a[1] += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        a[0] += 1
    return a
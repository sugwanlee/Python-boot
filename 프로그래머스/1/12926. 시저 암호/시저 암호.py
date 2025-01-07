def solution(s, n):
    aski = list(s)
    aski = list(map(lambda x : ord(x), aski))
    b = list(range(65,91)) + list(range(65,91)) + list(range(65,91))*(n//25)
    c = list(range(97,123)) + list(range(97,123)) + list(range(65,91))*(n//25)
    answer = []
    for i in aski:
        if i in b:
            answer.append(b[b.index(i) + n])
        elif i in c:
            answer.append(c[c.index(i) + n])
        else:
            answer.append(32)
    answer = ''.join(map(chr,answer))
    # aski_num = list(map(lambda x : ord(x)+n, aski))
    
    return answer
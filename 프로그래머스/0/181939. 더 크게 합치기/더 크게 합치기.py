def solution(a, b):
    c = int(str(a)+str(b))
    d = int(str(b)+str(a))
    e = [c, d]
    e.sort()
    if c == d:
        answer = c
    else:
        answer = e[1]
    return answer
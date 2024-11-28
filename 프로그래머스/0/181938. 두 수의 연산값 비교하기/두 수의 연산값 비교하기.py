def solution(a, b):
    c = int(str(a)+str(b))
    d = 2*a*b
    e = [c,d]
    e.sort()
    if c == d:
        answer = int(c)
    elif c != d:
        answer = e[1]
    return answer
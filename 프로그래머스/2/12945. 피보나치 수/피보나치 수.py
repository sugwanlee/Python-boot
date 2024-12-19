def solution(n):
    a = 1
    b = 1
    c = [0]  
    for i in range(n):
        (a, b) = (b+a, a)
        c.append(b)
    return c[n-1] % 1234567
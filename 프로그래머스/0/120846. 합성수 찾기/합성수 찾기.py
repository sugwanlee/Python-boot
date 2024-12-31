def solution(n):
    a = 0
    for i in range(1,n+1):
        for j in range(2,i):
            if i == 1:
                pass
            elif (i%j) == 0:
                a += 1
                break
    return a
        
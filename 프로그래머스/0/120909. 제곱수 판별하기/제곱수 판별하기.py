def solution(n):
    if (n % (n**(1/2))) == 0:
        answer = 1
    else:
        answer = 2
    return answer
def solution(a, b):
    answer = 0
    if (a % 2 == 1) & (b % 2 == 1):
        answer = a**2+b**2
    elif (a % 2 == 1) ^ (b % 2 == 1):
        answer = 2*(a+b)
    elif (a % 2 == 1) or not (b % 2 == 1):
        answer = abs(a-b)
    return answer
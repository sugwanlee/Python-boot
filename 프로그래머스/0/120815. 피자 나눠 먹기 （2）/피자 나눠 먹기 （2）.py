def solution(n):
    if (n % 6) == 0:
        answer = n / 6
    elif (n % 6) == 3:
        answer = (n * 2) / 6
    elif ((n % 6) == 2) or ((n % 6) == 4):
        answer = (n * 3) / 6
    else:
        answer = (n * 6) / 6
    return answer
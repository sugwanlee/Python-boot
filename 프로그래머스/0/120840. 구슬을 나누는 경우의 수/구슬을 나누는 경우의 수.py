def solution(balls, share):
    answer = 1
    for i in range(share+1, balls+1):
        answer = answer * i
    for j in range(1, balls-share+1):
        answer = answer // j
    return answer
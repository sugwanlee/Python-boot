def solution(i, j, k):
    answer = ""
    a = 0
    for i in range(i,j+1):
        answer += str(i)
    for i in answer:
        if i == f'{k}':
            a += 1
    return a
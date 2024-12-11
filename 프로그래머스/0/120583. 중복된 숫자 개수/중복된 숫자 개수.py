def solution(array, n):
    answer = []
    for i in array:
        if i == n:
            answer.append(i)
    return len(answer)
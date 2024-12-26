def solution(numLog):
    answer = ''
    for i, j in zip(numLog, numLog[1:]):
        if j-i == 1:
            answer += 'w'
        elif j-i == -1:
            answer += 's'
        elif j-i == 10:
            answer += 'd'
        elif j-i == -10:
            answer += 'a'
    return answer
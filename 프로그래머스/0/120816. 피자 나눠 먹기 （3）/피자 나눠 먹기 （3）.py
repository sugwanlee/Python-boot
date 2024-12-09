def solution(slice, n):
    answer = 0
    while True:
        answer += 1
        if (answer * slice) >= n:
            break
    return answer
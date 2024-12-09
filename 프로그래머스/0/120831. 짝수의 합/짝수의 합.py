def solution(n):
    m = n - 1
    s = n / 2
    while True:
        s = n / 2
        if s % 2 == 0:
            answer = (n + 2) * (s / 2)
            break
        elif s % 2 == 1:
            answer = (n + 2) * (s // 2) + n / 2 + 1
            break
        elif n % 2 == 1:
            n = m
            continue
    return answer
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        d = int(i[s:(s+l)])
        if d > k:
            answer.append(d)
    return answer
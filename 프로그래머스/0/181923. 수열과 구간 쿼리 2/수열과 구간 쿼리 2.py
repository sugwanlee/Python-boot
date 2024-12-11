def solution(arr, queries):
    answer = []
    for i in queries:
        a = sorted(arr[i[0]:i[1]+1])
        for b in a:
            if b > i[2]:
                answer.append(b)
                break
            elif b == a[-1]:
                answer.append(-1)
    return answer
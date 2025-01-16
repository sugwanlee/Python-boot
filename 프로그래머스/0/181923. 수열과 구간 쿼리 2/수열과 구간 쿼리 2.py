def solution(arr, queries):
    answer = []
    a = []
    for s, e, k in queries:
        for i, j in enumerate(arr):
            if (i >= s) and (i <= e) and (j > k):
                a.append(j)
        if a != []:
            answer.append(min(a))
            a = []
        else:
            answer.append(-1)
    return answer
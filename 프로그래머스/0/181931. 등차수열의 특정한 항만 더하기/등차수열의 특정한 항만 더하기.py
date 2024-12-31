def solution(a, d, included):
    b = 0
    list_1 = list(range(a,a+len(included)*d,d))
    for i, j in enumerate(list_1):
        if included[i] == True:
            b+=j
    return b
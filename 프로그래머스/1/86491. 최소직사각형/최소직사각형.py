def solution(sizes):
    a = []
    b = []
    for i in sizes:
        if i[0] <= i[1]:
            (i[0], i[1]) = (i[1], i[0])
        a.append(i[0])
        b.append(i[1])
    answer = max(a)*max(b)
            
    return answer
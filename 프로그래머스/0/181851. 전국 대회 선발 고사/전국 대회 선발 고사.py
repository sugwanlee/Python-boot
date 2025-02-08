def solution(rank, attendance):
    num_tup = []
    for i, j in enumerate(rank):
        if attendance[i] == True:
            num_tup.append([j,i])
    a, b, c = sorted(num_tup)[:3]
    return ((10000*a[1])+(100*b[1])+c[1])
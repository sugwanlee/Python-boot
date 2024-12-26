def solution(n):
    list = []
    for i in range(n):
        list.append([0*n]*n)
    for i in range(n):
        for j in range(n):
            if [i,j] == [j,i]:
                list[i][j] = 1
    return list
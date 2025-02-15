def solution(dots):
    dots.sort()
    arr_1 = []
    arr_2 = []
    for i in range(1,4):
        arr_1.append((dots[0][0] - dots[i][0]) / (dots[0][1] - dots[i][1]))
    arr_2.append((dots[2][0] - dots[3][0]) / (dots[2][1] - dots[3][1]))
    arr_2.append((dots[1][0] - dots[3][0]) / (dots[1][1] - dots[3][1]))
    arr_2.append((dots[1][0] - dots[2][0]) / (dots[1][1] - dots[2][1]))
    for i, j in (zip(arr_1, arr_2)):
        if i == j:
            return 1
    return 0
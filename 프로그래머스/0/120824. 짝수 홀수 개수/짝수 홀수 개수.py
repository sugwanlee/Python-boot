def solution(num_list):
    a = 0
    b = 0
    for i in num_list:
        if (i % 2) != 1:
            a = a + 1
        elif (i % 2) == 1:
            b = b + 1
    return [a,b]
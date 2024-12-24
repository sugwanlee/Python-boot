def solution(num_list):
    a = 0
    for i in num_list:
        if i < 0:
            return num_list.index(i)
        elif i >= 0:
            a = -1
    return a
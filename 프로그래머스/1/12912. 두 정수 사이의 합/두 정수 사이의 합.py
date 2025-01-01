def solution(a, b):
    list_1 = [a, b]
    list_1.sort()
    return sum(range(list_1[0],list_1[1]+1))
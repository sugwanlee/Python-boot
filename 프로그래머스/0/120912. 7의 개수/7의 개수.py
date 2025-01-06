def solution(array):
    str_7 = ""
    for i in map(str,array):
        str_7 += i
    return str_7.count("7")
def solution(code):
    ret = ''
    mode = 0
    for i, j in enumerate(code):
        if mode == 0:
            if j == "1":
                mode = 1
            elif (i%2) == 0:
                ret += j
        else:
            if j == "1":
                mode = 0
            elif (i%2) == 1:
                ret += j
    if ret == '':
        return "EMPTY"
    return ret
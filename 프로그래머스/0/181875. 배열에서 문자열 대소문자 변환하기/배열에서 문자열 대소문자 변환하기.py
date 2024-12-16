def solution(strArr):
    return [n.upper() if (strArr.index(n) % 2) == 1 else n.lower() for n in strArr]
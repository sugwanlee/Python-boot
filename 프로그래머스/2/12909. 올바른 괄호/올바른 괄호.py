def solution(s):
    arr = []
    for i in s:
        if i == "(":
            arr.append(i)
        elif i == ")" and len(arr) == 0:
            return False
        else:
            arr.pop()
    if len(arr) != 0:
        return False
    return True
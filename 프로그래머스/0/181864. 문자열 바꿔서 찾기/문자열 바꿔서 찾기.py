def solution(myString, pat):
    a = ''
    for i in myString:
        if i == "A":
            a += "B"
        elif i == "B":
            a += "A"
    if pat in a:
        return 1
    else:
        return 0
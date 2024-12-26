def solution(strArr):
    answer = []
    for i in strArr:
        if 'ad' not in i:
            answer.append(i)
    return [x for x in strArr if 'ad' not in x]
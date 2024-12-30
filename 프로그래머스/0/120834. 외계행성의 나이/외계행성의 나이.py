def solution(age):
    answer = str(age)
    alpa = "abcdefghij"
    for i, j in enumerate(alpa):
        answer = answer.replace(str(i),j)
    return answer
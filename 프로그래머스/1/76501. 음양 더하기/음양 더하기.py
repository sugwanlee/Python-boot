def solution(absolutes, signs):
    answer = 0
    for i, j in enumerate(signs):
        if j:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
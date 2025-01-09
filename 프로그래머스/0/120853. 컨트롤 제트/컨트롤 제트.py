def solution(s):
    answer = 0
    s_list = s.split(" ")
    for i, j in enumerate(s_list):
        if j == "Z":
            answer -= int(s_list[i-1])
        else:
            answer += int(j)
    return answer
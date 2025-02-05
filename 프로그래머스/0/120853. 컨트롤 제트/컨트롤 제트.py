def solution(s):
    # 숫자를 더할 변수 선언
    answer = 0
    # 공백 기준으로
    s_list = s.split()
    for i, j in enumerate(s_list):
        if j == "Z":
            answer -= int(s_list[i-1])
        else:
            answer += int(j)
    return answer
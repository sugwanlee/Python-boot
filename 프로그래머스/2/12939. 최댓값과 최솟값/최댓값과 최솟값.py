def solution(s):
    answer = ""
    s_list = list(map(int,s.split(" ")))
    answer += str(min(s_list)) + " "
    answer += str(max(s_list))
    return answer
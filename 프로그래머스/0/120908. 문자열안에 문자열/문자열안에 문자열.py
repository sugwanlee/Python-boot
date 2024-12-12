def solution(str1, str2):
    if str2 in str1:
        answer = 1
    elif str2 not in str1:
        answer = 2
    return answer
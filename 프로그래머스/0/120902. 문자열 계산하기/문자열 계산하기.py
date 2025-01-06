def solution(my_string):
    splited_my_string = my_string.split()
    answer = int(splited_my_string[0])
    for i, j in enumerate(splited_my_string):
        if i == (len(splited_my_string)-1):
            break
        elif j == '+':
            answer += int(splited_my_string[i+1])
        elif j == '-':
            answer -= int(splited_my_string[i+1])
    return answer
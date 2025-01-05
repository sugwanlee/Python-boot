def solution(my_string):
    answer = 0
    number = "0"
    for i in my_string:
        if i in "0123456789":
            number += i
        else:
            answer += int(number)
            number = "0"
    answer += int(number)
    return answer
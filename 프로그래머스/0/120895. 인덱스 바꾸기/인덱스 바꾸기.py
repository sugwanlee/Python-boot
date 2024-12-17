def solution(my_string, num1, num2):
    my_string_1 = list(my_string)
    my_string_1[num1] = my_string[num2]
    my_string_1[num2] = my_string[num1]
    return ''.join(my_string_1)
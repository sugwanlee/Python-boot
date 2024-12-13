def solution(my_string):
    alpa = ["a", "e", "i", "o", "u"]
    for i in alpa:
        my_string = my_string.replace(i,'')
    return my_string
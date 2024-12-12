def solution(my_string, overwrite_string, s):
    over_len = len(overwrite_string)+s
    my_string = list(my_string)
    my_string[s:over_len] = list(overwrite_string)
    my_string = ''.join(my_string)
    return my_string
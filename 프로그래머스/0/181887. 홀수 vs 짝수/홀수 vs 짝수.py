def solution(num_list):
    answer = 0
    if sum(num_list[1::2]) <= sum(num_list[::2]):
        answer = sum(num_list[::2])
    elif sum(num_list[1::2]) > sum(num_list[::2]):
        answer = sum(num_list[1::2])
    return answer
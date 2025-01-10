def solution(left, right):
    answer = 0
    num_list = 0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if (i % j) == 0:
                num_list += 1
        if (num_list % 2) == 0:
            answer += i
            num_list = 0
        else:
            answer -= i
            num_list = 0
    return answer
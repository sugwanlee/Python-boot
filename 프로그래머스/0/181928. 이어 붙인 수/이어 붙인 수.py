def solution(num_list):
    a = []
    b = []
    for i in num_list:
        if (i % 2) == 0:
            a.append(str(i))
        elif (i % 2) == 1:
            b.append(str(i))
    a_1 = int(''.join(a))
    b_1 = int(''.join(b))
    
    return a_1 + b_1
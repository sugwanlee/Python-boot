def solution(l, r):
    answer = []
    for num in range(l,r+1):
        num_list= list(set(map(int, list(str(num)))))
        if (num_list == [0,5]) or (num_list == [5]):
            answer.append(num)
    if answer == []:
        return [-1]
    return answer
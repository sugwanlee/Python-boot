def solution(num, k):
    answer = 0
    num = str(num)
    k = str(k)
    if k in num:
        answer = num.find(k)+1
    else:
        answer = -1
    return answer
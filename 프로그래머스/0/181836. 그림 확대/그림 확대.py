def solution(picture, k):
    answer = []
    for i in picture:
        a = ''
        for j in i:
            a += j * k
        for b in range(k):
            answer.append(a)
        
    return answer
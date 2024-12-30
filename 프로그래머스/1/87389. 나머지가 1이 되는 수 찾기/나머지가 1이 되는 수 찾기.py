def solution(n):
    for i in range(1,1000):
        if (n % i) == 1:
            answer = i
            break
        else:
            answer = n-1
    return answer
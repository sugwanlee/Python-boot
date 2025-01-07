def solution(n):
    if (n % 2) == 0:
        answer = "수박" * (n//2)
    elif (n % 2) == 1:
        answer = "수"+"박수" * ((n-1)//2)
    return answer
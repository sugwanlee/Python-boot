def solution(n, k):
    x = n // 10
    answer = n * 12000 + (k-x) * 2000
    return answer
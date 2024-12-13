def solution(n):
    def mul_1(x):
        return x**2
    odd_n = list(range(1, n+1, 2))
    even_n = list(range(2, n+1, 2))
    if (n % 2) == 1:
        answer = sum(odd_n)
    elif (n % 2) == 0:
        answer = sum(list(map(mul_1, even_n)))
    return answer
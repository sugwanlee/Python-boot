def solution(ineq, eq, n, m):
    comparison_operator = (''.join([ineq, eq]))
    if comparison_operator == ">=":
        if n >= m:
            answer = 1
        else:
            answer = 0
    elif comparison_operator == "<=":
        if n <= m:
            answer = 1
        else:
            answer = 0
    elif comparison_operator == "<!":
        if n < m:
            answer = 1
        else:
            answer = 0
    elif comparison_operator == ">!":
        if n > m:
            answer = 1
        else:
            answer = 0
    
    return answer
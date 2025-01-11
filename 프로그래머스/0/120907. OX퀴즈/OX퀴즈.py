def solution(quiz):
    answer = []
    for i in quiz:
        m, n = i.split('=')
        if eval(m) == int(n):
            answer.append("O")
        else:
            answer.append("X")
    return answer
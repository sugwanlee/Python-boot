def solution(picture, k):
    answer = []
    for i in picture:
        answer += [i.replace(".", "." * k).replace("x", "x" * k)] * k
    return answer
def solution(numbers):
    answer = [] 
    for i in numbers:
        for j in numbers:
            answer.append(i+j)
        answer.remove(i*2)
    return sorted(list(set(answer)))
def solution(myString):
    answer = ''
    for i in myString:
        if i in 'abcdefghijkl':
            answer += 'l'
        else:
            answer += i
    return answer
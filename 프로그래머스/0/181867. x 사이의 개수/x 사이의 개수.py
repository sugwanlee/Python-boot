def solution(myString):
    answer = myString.split('x')
    answer = list(map(lambda x:len(x),answer))
    return answer
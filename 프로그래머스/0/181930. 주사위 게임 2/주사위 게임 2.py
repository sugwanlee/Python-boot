def solution(a, b, c):
    list_1 = [a, b, c]
    list_2 = [a, b, c]
    if len(set(list_1)) == 1:
        answer = (a+b+c)*((a**2)+(b**2)+(c**2))*((a**3)+(b**3)+(c**3))
    elif len(set(list_1)) == 2:
        answer = (a+b+c)*(a*a+b*b+c*c)
    elif len(set(list_1)) == 3:
        answer = a+b+c
    
        
    


    return answer
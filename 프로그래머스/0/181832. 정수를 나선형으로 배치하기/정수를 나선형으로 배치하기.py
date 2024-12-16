def solution(n):
    answer = []
    

    if n == 1:
        return [[1]]
    
    for i in range(n) :
        answer.append([0]*n)
    
    x = 0
    y = 0
    dir = 'r'
    for i in range(1,n**2+1):
        if (dir == 'r'):
            answer[x][y] = i
            y +=1
            if answer[x][y] != 0:
                dir = 'd'
                y -= 1
                x += 1
            elif y == (n-1):
                dir = 'd'
            
                
        elif (dir == 'd'):
            answer[x][y] = i
            x +=1
            if answer[x][y] != 0:
                y -= 1
                x -= 1
                dir = 'l'    
            elif x == (n-1):
                dir = 'l'
        elif (dir == 'l'):
            answer[x][y] = i
            y -=1
            if answer[x][y] != 0:
                dir = 'u'
                y += 1
                x -= 1
            elif y == 0:
                dir = 'u'
        elif (dir == 'u'):
            answer[x][y] = i
            x -=1
            if answer[x][y] != 0:
                dir = 'r'
                x += 1
                y += 1
                    
    return answer
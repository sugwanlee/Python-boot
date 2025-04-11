m, n = map(int, input().split())
d = [[0]*n for _ in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
derection = 0

count = 0
def turn_right():
    global derection
    global count
    derection += 1
    count += 1
    if derection == 4:
        derection = 0
    
x = 0
y = 0
d[0][0] = 1

while True:
    nx = x+dx[derection]
    ny = y+dy[derection]
    if nx < m and nx >= 0 and ny < n and ny >= 0:
        if d[nx][ny] == 0:
            d[nx][ny] = 1
            x, y = nx, ny
        else:
            turn_right()
            nx = x+dx[derection]
            ny = y+dy[derection]
            if d[nx][ny] == 1:
                count -= 1
                break
    else:
        turn_right()
        nx = x+dx[derection]
        ny = y+dy[derection]
        if d[nx][ny] == 1:
            count -= 1
            break
            
if n == 1:
    count = 0        
print(count)
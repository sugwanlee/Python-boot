n, m = map(int, input().split())
r, c, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room = [list(map(int, input().split())) for _ in range(n)]
x, y = r, c

count = 0
while True:
    if room[x][y] == 0:
        room[x][y] = 2
        count += 1
    if room[x-1][y] != 0 and room[x][y+1] != 0 and room[x+1][y] != 0 and room[x][y-1] != 0:
        if d == 0:
            if room[x+1][y] != 1:
                x, y = x+1, y
            else:
                break
        elif d == 1:
            if room[x][y-1] != 1:
                x, y = x, y-1
            else:
                break
        elif d == 2:
            if room[x-1][y] != 1:
                x, y = x-1, y
            else:
                break
        elif d == 3:
            if room[x][y+1] != 1:
                x, y = x, y+1
            else:
                break
    else:
        d -= 1
        if d == -1:
            d = 3
        if room[x+dx[d]][y+dy[d]] == 0:
            x, y = x+dx[d], y+dy[d]
print(count)
        
            
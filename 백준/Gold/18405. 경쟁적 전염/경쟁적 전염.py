from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_idx = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_idx.append((graph[i][j], 0, i, j))
virus_idx.sort(key = lambda x: x[0])

queue = deque(virus_idx)

while queue:
    virus, time, a, b = queue.popleft()
    if time == s:
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((virus, time+1, nx, ny))

print(graph[x-1][y-1])
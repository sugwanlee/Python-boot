import copy

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(graph, x, y):
    if x <= -1 or x>= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 3
        dfs(graph, x-1, y)
        dfs(graph, x, y-1)
        dfs(graph, x+1, y)
        dfs(graph, x, y+1)
        return True
    return False

virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i, j])

cnt = 0
answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            for ii in range(i, n):
                for jj in range(m):
                    if graph[ii][jj] == 0:
                        for iii in range(ii, n):
                            for jjj in range(m):
                                if graph[iii][jjj] == 0:
                                    if len({(i, j), (ii, jj), (iii, jjj)}) < 3:
                                        continue
                                    cnt = 0
                                    test_graph = copy.deepcopy(graph)
                                    test_graph[i][j] = 1
                                    test_graph[ii][jj] = 1
                                    test_graph[iii][jjj] = 1
                                    for a, b in virus:
                                        test_graph[a][b] = 0
                                        dfs(test_graph, a, b)
                                    for c in test_graph:
                                        cnt += c.count(0)
                                    answer.append(cnt)
                                    
                    
print(max(answer))



    
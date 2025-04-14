from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
    
queue = deque([x])
nodes = [0] * (n + 1)


while queue:
    v = queue.popleft()
    for i in graph[v]:
        if i == x:
            continue
        if nodes[i] == 0:
            queue.append(i)
            nodes[i] = nodes[v] + 1
            
result = 0
for i, j in enumerate(nodes):
    if j == k:
        print(i)
        result += 1
if result == 0:
    print(-1)
        
n = int(input())
ropes = []
weights = []
for i in range(n):
    ropes.append(int(input()))
ropes.sort()
for i, j in enumerate(ropes):
    weights.append(j * (len(ropes) - i))
print(max(weights))
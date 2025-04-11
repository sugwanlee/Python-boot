n = int(input())
k = int(input())
pos = list(map(int, input().split()))
pos.sort()
dif = []
a = []
for i in range(n-1):
    dif.append(pos[i+1] - pos[i])
dif.sort(reverse=True)

print(sum(dif[k-1:]))
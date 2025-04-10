n, l = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

cnt = 1
length = 0
for i in range(n-1):
    length += pos[i+1] - pos[i]
    if length >= l:
        cnt += 1
        length = 0
print(cnt)
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0
for i in coins:
    count += k // i
    k %= i
    if k == 0:
        break
print(count)
n = int(input())
candys = [int(input()) for _ in range(n)]
total = sum(candys) // 2

a = total - sum(candys[1::2])
print(a)
for i in candys[:-1]:
    print(i-a)
    a = i-a
    
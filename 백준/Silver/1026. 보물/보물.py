k = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

answer = 0
for i in range(k):
    answer += a[i] * b[i]
print(answer)
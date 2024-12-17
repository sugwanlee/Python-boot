m = 0
x = int(input())
n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    m += a*b
if x == m:
    print("Yes")
if x != m:
    print("No")
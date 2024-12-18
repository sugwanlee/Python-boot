n = int(input())
a = [" "] * n
for i in range(n-1,-1,-1):
    a[i] = "*"
    print(''.join(a))
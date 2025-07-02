a = int(input())
b = list(map(int, input().split()))
c = max(b)
x = []
for i in b:
    x.append((i/c)*100)

print(sum(x)/a)
    
    
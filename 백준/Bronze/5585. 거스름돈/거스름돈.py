m = int(input())
c = 1000 - m
cnt = 0
for i in [500, 100, 50, 10 ,5 ,1]:
    cnt += c//i
    c %= i
    if c == 0:
        break
print(cnt)
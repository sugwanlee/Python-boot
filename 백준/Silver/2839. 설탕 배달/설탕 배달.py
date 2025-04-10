n = int(input())
count = 0
a = n // 5
count = 0
while True:
    if (a * 5) + (count * 3) == n:
        print(a + count)
        break
    elif (a * 5) + (count * 3) > n:
        count = 0
        a -= 1
    elif a == -1:
        print(-1)
        break
    count += 1
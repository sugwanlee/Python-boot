snum = list(range(1,31))

for i in range(28):
    snum.remove(int(input()))
snum.sort()
print(snum[0])
print(snum[1])
    
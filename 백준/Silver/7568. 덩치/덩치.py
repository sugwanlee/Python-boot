n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

rank = []
for h, w in people:
    rank.append(sum(1 for i in people if h < i[0] and w < i[1])+1)
print(" ".join(list(map(str, rank))))
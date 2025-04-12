array = [list(map(int, input().split())) for i in range(10)]
cards = [i for i in range(1, 21)]
for i, j in array:
    cards[i-1:j] = cards[i-1:j][::-1]
print(" ".join(map(str, cards)))
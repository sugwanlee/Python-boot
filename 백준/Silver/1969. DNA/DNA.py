from collections import Counter

n, m = map(int, input().split())
dna_array = []
array = []
for i in range(n):
    dna_array.append(input())
for i in range(m):
    ATGC_array = []
    for j in range(n):
        ATGC_array.append(dna_array[j][i])
    array.append(ATGC_array)
hd = 0
answer = ""
for i in array:
    counter = Counter(i)
    most_common = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    answer += most_common[0][0]
    hd += n - most_common[0][1]
print(answer)
print(hd)
    
        
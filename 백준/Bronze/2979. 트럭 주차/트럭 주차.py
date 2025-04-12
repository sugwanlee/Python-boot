a, b, c = map(int, input().split())
time_array = [0] * 100

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time_array[i] += 1
        
coast = 0
for i in time_array:
    if i == 1:
        coast += a
    elif i == 2:
        coast += 2 * b
    elif i == 3:
        coast += 3 * c
print(coast)
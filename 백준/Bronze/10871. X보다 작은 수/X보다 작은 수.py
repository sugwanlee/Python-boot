a, b = map(int, input().split())
num_list = map(int, input().split())
array = []
for num in num_list:
    if num < b:
        array.append(str(num))
print(" ".join(array))
        
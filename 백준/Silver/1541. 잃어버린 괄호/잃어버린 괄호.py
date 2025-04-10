exp = input().split("-")
answer = sum(map(int, exp[0].split("+")))
for i in exp[1:]:
    answer -= sum(map(int,i.split("+")))
print(answer)
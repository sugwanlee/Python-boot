count = 0
polys = []
poly = ""
for i in input():
    if poly == "":
        pass
    elif i == "X":
        if poly[0] == ".":
            polys.append(poly)
            poly = ""
    elif i == ".":
        if poly[0] == "X":
            polys.append(poly)
            poly = ""
    poly += i
polys.append(poly)
answer = ""
for i in polys:
    if i[0] == "X":
        if len(i) % 4 == 0:
            answer += len(i) * "A"
        elif len(i) % 4 == 2:
            answer += (len(i) - 2) * "A"
            answer += "BB"
        else:
            answer = "-1"
            break
        
    elif i[0] == ".":
        answer += i
print(answer)
    
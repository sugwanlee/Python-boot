def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x_count = 0
    num_count = 0
    for i in polynomial:
        if "x" == i:
            x_count += 1
        elif "x" in i:
            x_count += int(i[:-1])
        else:
            num_count += int(i)
    if x_count == 0:
        return f"{num_count}"
    elif num_count == 0 and x_count == 1:
        return f"x"
    elif num_count == 0:
        return f"{x_count}x"
    elif x_count == 1:
        return f"x + {num_count}"
    return f"{x_count}x + {num_count}"

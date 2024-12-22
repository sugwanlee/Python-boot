def solution(binomial):
    a, b, c= binomial.split()
    a = int(a)
    c = int(c)
    if "*" == b:
        return a*c
    elif "-" == b:
        return a-c
    elif "+" == b:
        return a+c
     
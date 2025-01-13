def solution(price, money, count):
    difference = 0
    for i in range(1,count+1):
        difference += i*price
    answer = difference - money
    if answer < 0:
        return 0
    return difference - money
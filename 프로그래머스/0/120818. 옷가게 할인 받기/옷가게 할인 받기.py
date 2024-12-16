def solution(price):
    if price < 100000:
        return price    
    elif price >= 500000:
        return  int(price - (price / 5))
    elif price >= 300000:
        return  int(price - (price / 10))
    elif price >= 100000:
        return  int(price - (price / 20))
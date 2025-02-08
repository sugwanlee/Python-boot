def solution(a, b, c, d):
    all_dice = [a, b, c, d]
    a_count = all_dice.count(a)
    b_count = all_dice.count(b)
    c_count = all_dice.count(c)
    d_count = all_dice.count(d)
    if set(all_dice) == {a}:
        return a * 1111
    elif a_count == 3 or b_count == 3 or c_count == 3 or c_count == 3:
        if a_count == 1:
            return (10 * b + a)**2
        elif b_count == 1:
            return (10 * a + b)**2
        elif c_count == 1:
            return (10 * b + c)**2
        elif d_count == 1:
            return (10 * b + d)**2
    
    elif (a_count == 2) and (b_count == 2) and (c_count == 2) and (c_count == 2):
        return (list(set(all_dice))[0] + list(set(all_dice))[1]) * abs(list(set(all_dice))[0] - list(set(all_dice))[1])
    
    elif len(set(all_dice)) == 3:
        if a_count == 2:
            p, q = list(set(all_dice)-{a})
            return p * q
        elif b_count == 2:
            p, q = list(set(all_dice)-{b})
            return p * q
        elif c_count == 2:
            p, q = list(set(all_dice)-{c})
            return p * q
        elif d_count == 2:
            p, q = list(set(all_dice)-{d})
            return p * q
        
    elif len(set(all_dice)) == 4:
        return min(all_dice)
        
    
        
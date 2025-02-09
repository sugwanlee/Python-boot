def solution(numer1, denom1, numer2, denom2):
    numer, denom = numer1* denom2 + numer2* denom1, denom1 * denom2
    for i in range(denom, 0, -1):
        if numer % i == 0 and denom % i == 0:
            numer, denom = numer//i, denom//i    
    return numer, denom
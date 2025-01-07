def solution(s):
    half_len = len(s) // 2 
    if (len(s) % 2) == 1:
        return s[half_len]
    else:
        return s[half_len-1:half_len+1]
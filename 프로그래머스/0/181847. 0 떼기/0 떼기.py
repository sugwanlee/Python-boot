def solution(n_str):
    answer = ''
    for i in n_str:
        if i == '0':
            n_str = n_str.replace('0','',1)
        else:
            break        
    return n_str
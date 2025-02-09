def solution(array):
    while len(set(array)) != 1:
        for i in set(array):
            array.remove(i)
        if len(array) == 1:
            return array[0]
        elif len(set(array)) == len(array):
            return -1
    return array[0]
    
        
    
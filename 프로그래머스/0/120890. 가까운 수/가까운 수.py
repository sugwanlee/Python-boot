def solution(array, n):
    array.append(n)
    array.sort()
    a = array.index(n)
    if array[-1] == n:
        return array[a-1]
    else:
        if (n-array[a-1]) == (array[a+1] - n):
            return array[a-1]
        elif (n-array[a-1]) > (array[a+1] - n):
            return array[a+1]
        elif (n-array[a-1]) < (array[a+1] - n):
            return array[a-1]
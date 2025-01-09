def solution(arr):
    if 2 in arr:
        first_2 = arr.index(2)
        second_2 = arr[::-1].index(2)
        if arr[-1] == 2:
            return arr[first_2:]
        else:
            return arr[first_2:-second_2]
    else:
        return [-1]
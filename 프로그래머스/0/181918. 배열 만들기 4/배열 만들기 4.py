def solution(arr):
    stk = []
    i = 0
    while len(arr) != i:
        if stk == []:  
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            del stk[-1]
    return stk
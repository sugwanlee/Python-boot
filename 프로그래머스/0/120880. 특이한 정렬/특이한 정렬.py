def solution(numlist, n):
    answer = []
    arr = [i-n for i in numlist]
    arr_abs = sorted([abs(i-n) for i in numlist])
    for i in arr_abs:
        if i in arr:
            answer.append(numlist[arr.index(i)])
            arr[arr.index(i)] = "dummy"
        elif -i in arr:
            answer.append(numlist[arr.index(-i)])
            arr[arr.index(-i)] = "dummy"
    return answer
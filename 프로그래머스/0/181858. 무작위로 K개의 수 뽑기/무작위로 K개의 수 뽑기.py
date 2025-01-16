def solution(arr, k):
    set_arr = []
    for i in arr:
        if i not in set_arr:
            set_arr.append(i)
    if len(set_arr) >= k:
        return set_arr[:k]
    else:
        set_arr += [-1] * (k - len(set_arr))
        return set_arr
    
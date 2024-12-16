def solution(arr, k):
    return [k*n if (k % 2) == 1 else n+k for n in arr ]
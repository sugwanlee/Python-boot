def solution(A, B):
    count = 0
    while A != B:
        A = A[-1] + A[:-1]
        count += 1
        if count > len(A):
            return -1
    return count
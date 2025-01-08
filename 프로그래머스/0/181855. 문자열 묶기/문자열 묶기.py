def solution(strArr):
    ans = [0] * len(strArr)
    for s in strArr:
        ans[len(s)] += 1
    return max(ans)
    
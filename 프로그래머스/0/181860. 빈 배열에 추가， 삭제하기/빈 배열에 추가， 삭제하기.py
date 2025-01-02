def solution(arr, flag):
    answer = []
    for i, j in enumerate(flag):
        if j:
            for m in range(arr[i]):
                answer.append(arr[i])
                answer.append(arr[i])
        else:
            answer = answer[0:-arr[i]]
    return answer
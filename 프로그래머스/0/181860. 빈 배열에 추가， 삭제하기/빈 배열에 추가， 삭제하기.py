def solution(arr, flag):
    answer = []
    for i, j in enumerate(flag):
        if j == True:
            for m in range(arr[i]):
                answer.append(arr[i])
                answer.append(arr[i])
        elif j == False:
            answer = answer[0:-arr[i]]
    return answer
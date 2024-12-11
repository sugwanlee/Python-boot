def solution(arr, queries):
    answer = []
    for i in queries:
        for b in arr:
            if (arr[i[0]] <= b) and (arr[i[1]] >= b) and (arr[i[2]] < b):
                answer.append(b)
                break
            elif b == arr[len(arr)-1]:
                answer.append(-1)
                break
    return answer
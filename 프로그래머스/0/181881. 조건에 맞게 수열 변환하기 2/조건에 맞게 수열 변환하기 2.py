def solution(arr):
    answer = 0    
    while True:
        compare = arr.copy()
        for i, j in enumerate(arr):
            if (j >= 50) and (j % 2) == 0:
                arr[i] = j // 2
            elif (j < 50) and (j % 2) == 1:
                arr[i] = (j * 2) + 1
        if compare == arr:
            break
        answer += 1
        
    return answer
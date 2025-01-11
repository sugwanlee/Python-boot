def solution(n):
    measure = []
    measure_1 = 0
    answer = []
    for i in range(1,n+1):
        if (n % i) == 0:
            measure.append(i)
    for i in measure:
        for j in range(1,i+1):
            if (i % j) == 0:
                measure_1 += 1
        if measure_1 == 2:
            answer.append(i)
        measure_1 = 0    
    return answer
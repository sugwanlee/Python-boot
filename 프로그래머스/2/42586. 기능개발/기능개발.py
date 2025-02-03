def solution(progresses, speeds):
    answer = []
    count = 0
    while True:
        progresses = [x + y for x, y in zip(progresses, speeds)]
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if progresses == []:
                answer.append(count) 
                return answer
            elif progresses[0] < 100:
                answer.append(count)
                count = 0
    
def solution(k, score):
    answer = []
    hall_score = []
    for i, j in enumerate(score, 1):
        if i <= k:
            hall_score.append(j)
            hall_score.sort()
        elif j > hall_score[0]:
            hall_score.pop(0)
            hall_score.append(j)
            hall_score.sort()
        answer.append(hall_score[0])
        
    return answer
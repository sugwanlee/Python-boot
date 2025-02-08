def solution(score):
    score_avr = [sum(i) / 2 for i in score]
    score_avr_reversed = sorted(score_avr, reverse=True)
    return [score_avr_reversed.index(i)+1 for i in score_avr]
        
def solution(keyinput, board):
    answer = [0, 0]
    for arrow in keyinput:
        if arrow == "up" and answer[1] != board[1]//2:
            answer[1] += 1
        if arrow == "down" and answer[1] != -(board[1]//2):
            answer[1] -= 1
        if arrow == "left" and answer[0] != -(board[0]//2):
            answer[0] -= 1
        if arrow == "right" and answer[0] != board[0]//2:
            answer[0] += 1
    return answer
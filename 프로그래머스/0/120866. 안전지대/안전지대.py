def solution(board):
    answer = 0
    row = len(board)
    for i in range(row):
        board[i] = [0] + board[i] +[0]
    col = len(board[0])
    board = [[0]*col] + board + [[0]*col]
    row = len(board)
    col = len(board[0])
    for i in range(1,row-1):
        for j in range(1, col-1):
            if board[i][j] == 1:
                continue
            for row_offset in [-1, 0, 1]:
                for col_offset in [-1, 0, 1]: 
                    if row_offset == 0 and col_offset == 0:
                        continue
                    elif board[i + row_offset][j + col_offset] == 1:
                        board[i][j] = 2
            if board[i][j] == 0:
                answer += 1
                

    return answer
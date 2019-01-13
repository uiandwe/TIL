def solution(board):

    retMax = 0
    row = len(board)
    col = len(board[0])

    d = [[0 for y in range(col+1)] for x in range(row+1)]

    for i in range(1, row+1):
        for j in range(1, col+1):
            if board[i-1][j-1] > 0:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1])+1
                retMax = max(retMax, d[i][j])

    return retMax*retMax 

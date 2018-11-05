https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3


block_x = [0, 1, 1]
block_y = [1, 0, 1]

def rotationBlock(m, n, board):
    returnArray = []
    for i in range(n-1, -1, -1):
        temp = []
        for j in range(m):
            temp.append(board[j][i])
        returnArray.append(temp)
    return returnArray


def blockGroup(m, n, board):
    copy_board = []
    loop = False

    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(board[i][j])
        copy_board.append(temp)

    for i in range(0 ,n-1):
        for j in range(0, m-1):
            checkChar = board[i][j]
            if checkChar != 0 and board[i+block_y[0]][j+block_x[0]] == checkChar and board[i + block_y[1]][j + block_x[1]] == checkChar and board[i + block_y[2]][j + block_x[2]] == checkChar :
                copy_board[i][j] = 0
                copy_board[i][j+1] = 0
                copy_board[i+1][j] = 0
                copy_board[i+1][j+1] = 0
                loop = True

    if loop is True:
        board = pushBlock(copy_board)
        return blockGroup(m, n, board)
    else:
        return board


def pushBlock(board):
    returnArray = []
    for i in board:
        countZero = 0
        for j in i:
            if j == 0:
                countZero += 1
        i = list(filter(lambda a: a != 0, i))
        for j in range(countZero):
            i.insert(0, 0)
        returnArray.append(i)
    return returnArray


def solution(m, n, board):
    answer = 0

    d = rotationBlock(m, n, board)

    board = blockGroup(m, n, d)

    for i in board:
        for j in i:
            if j == 0:
                answer += 1

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

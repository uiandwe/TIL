# -*- coding: utf-8 -*-
# https://www.welcomekakao.com/learn/courses/30/lessons/12905


def solution(board):
    answer = 0

    row = len(board)
    col = len(board[0])

    for i in range(0, row):
        for j in range(0, col):
            answer = max(board[i][j], answer)
            if board[i][j] > 0 and i > 0 and j > 0:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
                answer = max(answer, board[i][j])
    return answer*answer


def test_solution():
    assert solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) == 9
    assert solution([[0,0,1,1],[1,1,1,1]]) == 4
    assert solution([[0, 1, 0], [1, 1, 1], [0, 1, 0]]) == 1
    assert solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 1
    assert solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 9
    assert solution([[0, 1, 1], [1, 1, 1], [1, 1, 1]]) == 4
    assert solution([[1, 1, 1], [0, 1, 1], [1, 1, 1]]) == 4
    assert solution([[1, 1, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]) == 9
    assert solution([[1, 0], [0, 0]]) == 1
    assert solution([[0, 0], [0, 0]]) == 0
    assert solution([[1]]) == 1
    assert solution([[0]]) == 0
    assert solution([[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]]) == 9
    assert solution([[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1]]) == 9
    assert solution([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]) == 9
    assert solution([[1, 1, 1, 1]]) == 1
    assert solution([[0, 1, 0, 0]]) == 1
    assert solution([[0, 0, 0, 0]]) == 0
    assert solution([[0], [0], [0], [0]]) == 0
    assert solution([[1], [0], [0], [0]]) == 1
    assert solution([[1], [0]]) == 1
    assert solution([[1, 1]]) == 1
    assert solution([[0, 1]]) == 1
    assert solution([[1, 0]]) == 1
    assert solution([[0, 0]]) == 0


print(solution([[0], [0], [0], [0]]))

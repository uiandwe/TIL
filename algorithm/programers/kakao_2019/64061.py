# -*- coding: utf-8 -*-
class Stack:
    __slots__ = ['array']

    def __init__(self):
        self.array = []

    def __repr__(self):
        return str(self.array)

    def push(self, value: int):
        self.array.append(value)

    def pop(self)-> int:
        if self.empty() is False:
            return self.array.pop()
        else:
            return -1

    def size(self):
        return len(self.array)

    def empty(self):
        if len(self.array) > 0:
            return False
        else:
            return True

    def top(self):
        if self.empty():
            return -1
        else:
            return self.array[self.size() - 1]


def get_board_top(board, move_line):
    h = len(board)
    ret_top = -1

    for y in range(h):
        if board[y][move_line-1] > 0:
            ret_top = board[y][move_line-1]
            board[y][move_line - 1] = 0
            break

    return ret_top

def solution(board, moves):
    answer = 0
    s = Stack()

    for move in moves:
        crane = get_board_top(board, move)
        if crane != -1:
            if not s.empty() and s.top() == crane:
                s.pop()
                answer += 2
            else:
                s.push(crane)

    return answer



solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])

# -*- coding: utf-8 -*-
# https://programmers.co.kr/learn/courses/30/lessons/42585

class Stack(object):
    def __init__(self):
        self._stack_array = []
        self._count = 0
        self._stack_count = 0

    def push(self, c):
        if c == ')':
            # 레이저
            if self._stack_array[-1] == '(':
                self._stack_count -= 1 # 막대기가 아니므로 하나를 뺀다
                self._count += self._stack_count
            # 막대기 끝
            else:
                self._stack_count -= 1
                self._count += 1
        # 막대기 시작
        else:
            self._stack_count += 1
        self._stack_array.append(c)

    @property
    def total(self):
        return self._count


def solution(arrangement):
    s = Stack()
    for val in arrangement:
        s.push(val)

    return s.total

def test_solution():
    assert solution("()(((()())(())()))(())") == 17
    assert solution("()") == 0
    assert solution("(())") == 2
    assert solution("((()))") == 4
    assert solution("(((())))") == 6
    assert solution("(()())") == 3
    assert solution("((()()))") == 6
    assert solution("(((()())))") == 9



print(solution("()(((()())(())()))(())"))

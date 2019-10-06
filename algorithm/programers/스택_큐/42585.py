# https://programmers.co.kr/learn/courses/30/lessons/42585
class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.array.pop()

    def size(self):
        return len(self.array)

    def empty(self):
        return True if self.size() <= 0 else False

    def top(self):
        if self.empty():
            return False
        else:
            return self.array[-1]


def solution(arrangement):
    answer = 0

    s = Stack()

    for index, c in enumerate(arrangement):
        if c == ")":
            s.pop()
            if arrangement[index - 1] == "(":  # 레이저
                answer += s.size()
            else:  # 막대
                answer += 1
        else:
            s.push(c)

    return answer


assert solution("(())") == 2
assert solution("(()())") == 3
assert solution("(())(())") == 4
assert solution("((())(()))") == 7
assert solution("((())(()))") == 7
assert solution("((())()(()))") == 8
assert solution("(())(()())") == 5

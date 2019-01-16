class Stack:

    def __init__(self):
        self.array = []

    def push(self, num):
        self.array.append(num)

    def pop(self):
        if self.empty() is False:
            return self.array.pop()
        else:
            return -1

    def size(self):
        return len(self.array)

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True


def solution(str):

    s = Stack()

    for c in str:
        if c == "(":
            s.push(c)
        else:
            if s.pop() == -1:
                return "NO"

    if s.empty():
        return "YES"
    else:
        return "NO"

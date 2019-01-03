class stack:

    def __init__(self):
        self.array = []

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.array.pop()

    def push(self, data):
        self.array.append(data)

    def top(self):
        if self.empty():
            return -1
        else:
            return self.array[self.size()-1]

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)


def solution(str):
    s = stack()
    for c in str:
        if s.top() != -1 and s.top() == '{' and c == '}':
            s.pop()
        else:
            s.push(c)

    retInt = 0
    while s.empty() is False:
        c1 = s.pop()
        c2 = s.pop()

        if c1 != c2:
            retInt += 2
        else:
            retInt += 1

    return retInt

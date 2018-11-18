class stack:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty():
            return self.array.pop(self.size()-1)
        else:
            return False

    def size(self):
        return len(self.array)

    def empty(self):
        if self.size() > 0:
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            return self.array[self.size()-1]
        else:
            return False


class stackQueue:
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()

    def push(self, data):
        while self.s2.empty():
            temp = self.s2.pop()
            self.s1.push(temp)

        self.s1.push(data)

        while self.s1.empty():
            temp = self.s1.pop()
            self.s2.push(temp)

    def pop(self):
        if self.s2.empty():
            return self.s2.pop()
        else:
            return False

    def empty(self):
        return self.s2.empty()

    def peek(self):
        return self.s2.peek()


def solution():
    sq = stackQueue()
    sq.push(1)
    sq.push(2)
    print(sq.peek())
    print(sq.pop())
    print(sq.pop())
    print(sq.empty())


solution()

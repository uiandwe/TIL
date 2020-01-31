# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


class Stack:
    def __init__(self):
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        return self.__list.pop()

    def size(self):
        return len(self.__list)

    def empty(self):
        return True if self.size() <= 0 else False

    def peck(self):
        return self.__list[self.size()-1]


def solution(A, B):
    s = Stack()
    ret_val = 0

    for i, j in zip(A, B):
        if j == 0:
            ret_val += 1
            if s.empty():
                continue
            while s.empty() is False:
                ret_val -= 1
                if s.peck() > i:
                    break
                else:
                    s.pop()
        else:
            ret_val += 1
            s.push(i)

    return ret_val


solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])

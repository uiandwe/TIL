import sys

class stack:
    def __init__(self):
        self.array = []
        self.minIndex = -1
        self.minValue = sys.maxsize

    def initMin(self):
        self.minIndex = -1
        self.minValue = sys.maxsize

    def push(self, data):
        self.array.append(data)
        if self.minValue > data:
            self.minValue = data
            self.minIndex = self.size()-1

    def pop(self):
        if self.empty() is False:
            returnValue = self.array.pop(self.size() - 1)
            self.initMin()

            for i in range(self.size()):
                if self.minValue > self.array[i]:
                    self.minValue = self.array[i]
                    self.minIndex = i
                    break

            return returnValue
        else:
            return False

    def size(self):
        return len(self.array)
    
    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def peek(self):
        if self.empty() is False:
            return self.array[self.size()-1]
        else:
            return False

    def getMin(self):
        if self.empty() is False:
            return self.minValue
        else:
            return False


def solution():
    minStack = stack()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())



solution()

class stack:
    array = []

    def __init__(self):
        self.array = []

    def pop(self):
        if self.empty() is False:
            return self.array.pop(self.size()-1)
        else:
            return -1

    def push(self, val):
        return self.array.append(val)

    def top(self):
        if self.empty() is False:
            point = self.size()-1
            return self.array[point]
        else:
            return -1


    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.array)

class Queue:
    array = []

    def push(self, num):
        self.array.append(num)

    def pop(self):
        if self.size() > 0:
            return self.array.pop(0)

    def size(self):
        return len(self.array)

    def empty(self):
        if len(self.array) > 0:
            return False
        else:
            return True

    def front(self):
        if self.size() > 0:
            return self.array[0]

    def back(self):
        if self.size() > 0:
            top = self.size()
            return self.array[top-1]

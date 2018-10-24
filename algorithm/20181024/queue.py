class queue:

    array = []

    def push(self, val):
        return self.array.insert(0, val)

    def pop(self):
        if self.emtpy() is False:
            return self.array.pop(self.size()-1)
        else:
            return -1

    def size(self):
        return len(self.array)

    def emtpy(self):
        if self.size() == 0:
            return True
        else:
            return False

    def front(self):
        if self.emtpy() is False:
            return self.array[self.size()-1]
        else:
            return -1

    def back(self):
        if self.emtpy() is False:
            return self.array[0]
        else:
            return -1

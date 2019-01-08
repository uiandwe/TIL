import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.array = []

    def insert(self, val):
        if val in self.dict:
            return False
        else:
            self.dict[val] = 1
            self.array.append(val)
            return True

    def remove(self, val):
        if val in self.dict:
            del self.dict[val]
            self.array.pop(self.array.index(val))
            return True
        else:
            return False

    def getRandom(self):
        if len(self.array) > 0:
            r = random.randrange(0, len(self.array))
            return self.array[r]
        else:
            return False

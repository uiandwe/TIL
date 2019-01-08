import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.array = []

    def insert(self, val):
        if val in self.dict:
            return False
        else:
            self.array.append(val)
            self.dict[val] = len(self.array)-1

            return True

    def remove(self, val):
        if val in self.dict:
            self.array.pop(self.dict[val])
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self):
        if len(self.array) > 0:
            r = random.randrange(0, len(self.array))
            return self.array[r]
        else:
            return False

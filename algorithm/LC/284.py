# -*- coding: utf-8 -*-
class PeekingIterator:
    def __init__(self, iterator):
        self.d = []
        while iterator.hasNext():
            self.d.append(iterator.next())
        self.i = 0

    def peek(self):
        return self.d[self.i]

    def next(self):
        ret_val = self.d[self.i]
        self.i += 1
        return ret_val

    def hasNext(self):
        if len(self.d) > self.i:
            return True
        return False


class PeekingIterator:
    def __init__(self, iterator):
        self.d = iterator
        self.i = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.i

    def next(self):
        temp = self.i
        self.i = self.d.next() if self.d.hasNext() else None
        return temp

    def hasNext(self):
        return True if self.i else False

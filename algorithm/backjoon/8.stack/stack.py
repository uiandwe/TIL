class Stack(object):
    def __init__(self):
        self.arr = []

    def push(self, value):
        if isinstance(value, list):
            for v in value:
                self.arr.append(v)
        elif isinstance(value, int):
            self.arr.append(value)

    def pop(self):
        if self.size() > 0:
            return self.arr.pop()
        else:
            return -1

    def size(self):
        return len(self.arr)


def test_stack():
    s = Stack()
    s.push([1, 2, 3])

    assert s.pop() == 3
    assert s.pop() == 2
    assert s.size() == 1

    s.push(10)

    assert s.size() == 2
    assert s.pop() == 10
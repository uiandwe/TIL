

class stack():
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(self.size()-1)
        else:
            return -1

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)

    def top(self):
        if self.empty() is False:
            return self.array[self.size()-1]
        else:
            return -1


def solution(array):
    d = [0]
    d += ([x for x in array])
    d.append(0)
    s = stack()
    s.push(0)
    ans = 0

    for i in range(1, len(d)):
        while s.empty() is False and d[s.top()] > d[i]:
            h = s.pop()
            w = i - s.top() -1
            ans = max(ans, h*w)
        s.push(i)
    print(ans)



solution([1, 2, 3])

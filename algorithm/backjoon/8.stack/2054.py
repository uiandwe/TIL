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


def solution(str):
    s = stack()
    for i in str:
        if i == "(" or i == "[":
            s.push(i)
        elif i == ")":
            c = s.top()
            if c == '(':
                s.pop()
                s.push(2)
            else:
                s.push(")")
        elif i == "]":
            c = s.top()
            if c == '[':
                s.pop()
                s.push(3)
            else:
                s.push("]")
    a = 0
    s1 = stack()
    while s.empty() is False:
        c = s.pop()

        if c == "[":
            a *= 3
        elif c == "(":
            a *= 2
        elif c == "]" or c == ")":
            if a > 0:
                s1.push(a)
                a = 0
        else:
            a += c

    while s1.empty() is False:
        c = s1.pop()
        a += c

    print(a)

solution("[()[()]]")
solution("([])")
solution("()[[]]")
solution("(()[[]])")
solution("(()[[]])([])")

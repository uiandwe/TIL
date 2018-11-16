class stack:
    array = []

    def push(self, c):
        self.array.append(c)

    def pop(self):
        if self.size() >= 0:
            return self.array.pop(0)
        else:
            return False

    def size(self):
        return len(self.array)


def solution(str):
    s = stack()
    for c in str:
        if c == '{' or c == '[' or c == '(':
            s.push(c)
        else:
            popChar = s.pop()
            if popChar is False:
                return False
            elif popChar == '}' and c != '{':
                return False
            elif popChar == ']' and c != '[':
                return False
            elif popChar == ')' and c != '(':
                return False

    if s.size() > 0:
        return False
    else:
        return True

print(solution("{[]}"))
print(solution("(())"))
print(solution("((()"))
print(solution("())"))

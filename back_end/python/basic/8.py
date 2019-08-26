# accessing items

class Stack:
    def __init__(self):
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        return self.__list.pop()

    def __repr__(self):
        return "{}".format(self.__list)

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, item):
        return self.__list[item]

    def __setitem__(self, key, value):
        self.__list[key] = value


s = Stack()
s.push(1)
s.push(2)
print("stack", s)

s[0] = 3
print(s)

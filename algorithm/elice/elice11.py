class stack:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.array.pop()

    def top(self):
        if self.empty():
            return -1
        else:
            return self.array[self.size()-1]

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)

class queue:
    array = []

    def push(self, num, position=-1):
        if position == -1:
            self.array.append(num)
        else:
            self.array.insert(0, num)

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


def calculator(a, b, symbol):
    if symbol == '+':
        return a + b
    elif symbol == '-':
        return a - b
    elif symbol == '*':
        return a * b
    elif symbol == '/':
        return a / b


def cal(data):
    q = queue()
    s = stack()
    temp_stack = stack()

    index = 0
    temp_val = ''
    while len(data) > index:
        c = data[index]

        #숫자만 처리
        if c != '+' and c != '-' and c != '*' and c != '/' and c != '(' and c!= ')':
            # 두자리 이상 처리 부분
            temp = ''
            while index < len(data):
                temp_c = data[index]
                if temp_c.isdigit():
                    temp += temp_c
                    index += 1
                else:
                    index -= 1
                    break

            s.push(temp)
        else:
            if c == ')':
                temp_symbol = ''
                temp_a = 0
                temp_b = 0
                retVal = 0
                while s.empty() is False:
                    temp_c = s.pop()
                    if temp_c == '(':
                        s.push(retVal)
                        break

                    if temp_c != '+' and temp_c != '-' and temp_c != '*' and temp_c != '/':
                        if temp_a == 0 and temp_b == 0:
                            temp_a = int(temp_c)
                        elif temp_a != 0 and temp_b == 0:
                            temp_b = int(temp_c)
                    else:
                        temp_symbol = temp_c

                    if temp_a != 0 and temp_b != 0 and temp_symbol != '':
                        if temp_symbol == '-':
                            retVal = calculator(temp_b, temp_a, temp_symbol)
                        else:
                            retVal = calculator(temp_a, temp_b, temp_symbol)
                        s.push(retVal)
                        temp_symbol = ''
                        temp_a = 0
                        temp_b = 0
            else:
                s.push(c)
        index += 1

    while s.empty() is False:
        temp_stack.push(s.pop())

    while temp_stack.empty() is False:
        q.push(temp_stack.pop())

    temp_a = 0
    temp_b = 0
    temp_symbol = ''
    retVal = 0

    if q.size() == 1:
        return q.pop()

    while q.empty() is False:
        temp_c = q.pop()

        if temp_c != '+' and temp_c != '-' and temp_c != '*' and temp_c != '/':
            if temp_a == 0 and temp_b == 0:
                temp_a = int(temp_c)
            elif temp_a != 0 and temp_b == 0:
                temp_b = int(temp_c)
        else:
            temp_symbol = temp_c

        if temp_a != 0 and temp_b != 0 and temp_symbol != '':
            retVal = calculator(temp_a, temp_b, temp_symbol)
            q.push(retVal, 0)
            temp_a = 0
            temp_b = 0
            temp_symbol = ''

    return "%0.1f" % retVal


def main():
    data = str(input())
    print(cal(data))


if __name__ == "__main__":
    main()

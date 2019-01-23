class queue:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(0)
        else:
            return -1

    def size(self):
        return len(self.array)

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True


def solution(num, step):
    ret_arr = []
    q = queue()

    for i in range(1, num+1):
        q.push(i)

    index = 0
    while q.empty() is False:
        index += 1
        pop_data = q.pop()
        if index % step == 0:
            ret_arr.append(pop_data)
        else:
            q.push(pop_data)

    return ret_arr

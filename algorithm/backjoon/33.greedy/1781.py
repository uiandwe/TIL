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

    def top(self):
        if self.empty() is False:
            return self.array[0]
        else:
            return -1

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)


def solution(array):
    q = queue()

    array = sorted(array,  key=lambda x:x[0])
    total_sum = 0
    for i in range(len(array)):
        if q.empty() is True:
            q.push(array[i])
        else:
            node = q.top()
            if node[0] == array[i][0]: #같은 데드라인
                if node[1] < array[i][1]:
                    q.pop()
                    q.push(array[i])
            else: #이미 지난 데드라인
                node = q.pop()
                total_sum += node[1]
                q.push(array[i])

    while q.empty() is False:
        node = q.pop()
        total_sum += node[1]

    print(total_sum)

solution([[1, 6], [1, 7], [3, 2], [3, 1], [2, 4], [2, 5], [6, 1]])
solution([[1, 20], [2, 25], [2, 30]])
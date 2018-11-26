class Queue:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(0)
        else:
            return False

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)


def solution(array):
    q = Queue()
    q.push(0)
    temp = []
    while q.empty() is False:
        point = q.pop()
        left = point * 2 + 1
        right = point * 2 + 2
        if left < len(array) and array[left] is not None:
            childLeft = left * 2 + 1
            if childLeft > len(array) or (len(array) > childLeft and array[childLeft] is None):
                temp.append(array[left])
            else:
                q.push(left)
        elif point % 2 == 1:
            temp.append(array[point])

        if right < len(array) and array[right] is not None:
            q.push(right)

    print(temp)

solution([3, 9, 20, 1, 2, 15, 7])

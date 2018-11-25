class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def push(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if node.data > data:
                node.left = self.push(node.left, data)
            else:
                node.right = self.push(node.right, data)

        return node

    def pushNode(self, data):
        self.root = self.push(self.root, data)


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

    def printArray(self):
        temp = []
        for i in range(len(self.array)):
            temp.append(self.array[i])

        print(','.join([str(x.data) for x in self.array]))


def whileQueue(t, array):
    q = Queue()
    q.push(t.root)

    while q.empty()is False:
        array.append(q.array[q.size()-1].data)
        for i in range(q.size()):
            node = q.pop()
            if node.left is not None:
                q.push(node.left)
            if node.right is not None:
                q.push(node.right)


def solution(array):
    t = Tree()
    for i in array:
        t.pushNode(i)

    printArray = []

    whileQueue(t, printArray)
    print(printArray)


solution([4, 3, 1, 2, 8, 5, 9])

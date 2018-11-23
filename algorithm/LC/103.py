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

    def preOrder(self, node):
        if node.left is not None:
            self.preOrder(node.left)

        print(node.data)

        if node.right is not None:
            self.preOrder(node.right)

    def printPreOrder(self):
        self.preOrder(self.root)

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
    t = Tree()
    for i in array:
        t.pushNode(i)

    t.printPreOrder()

    q = Queue()
    q.push(t.root)

    while q.empty() is False:
        printArray = []
        for i in range(q.size()):
            node = q.pop()
            printArray.append(node.data)
            if node.left is not None:
                q.push(node.left)
            if node.right is not None:
                q.push(node.right)

        print(printArray)


solution([3, 4, 1, 2, 6])


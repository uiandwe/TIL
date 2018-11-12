class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class tree():
    root = None
    depth = 0
    tempDepth = 0

    def insert(self, node, value):
        if node is None:
            node = Node(value)
            if self.tempDepth > self.depth:
                self.depth = self.tempDepth
        else:
            self.tempDepth += 1
            if node.data > value:
                node.left = self.insert(node.left, value)
            else:
                node.right = self.insert(node.right, value)

        return node

    def insertNode(self, value):
        self.tempDepth = 0
        self.root = self.insert(self.root, value)

    def inOrder(self, node, array):
        if node is not None:
            if node.left:
                self.inOrder(node.left, array)

            array.append(node.data)

            if node.right is not None:
                self.inOrder(node.right, array)


def solution(array):
    t = tree()

    for i in array:
        t.insertNode(i)
    d = []
    t.inOrder(t.root, d)
    print(d)
    print(t.depth)

a = [2, 4, 1, 3, 9]

print(solution(a))

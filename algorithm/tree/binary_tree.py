class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class tree():
    root = None

    def insert(self, node, value):
        if node is None:
            node = Node(value)
        else:
            if node.data > value:
                node.left = self.insert(node.left, value)
            else:
                node.right = self.insert(node.right, value)

        return node

    def insertNode(self, value):
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

a = [2, 4, 1, 3, 9]

print(solution(a))

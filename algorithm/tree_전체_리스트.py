import copy

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


def backTrack(node, ret, array):


    array.append(node.data)

    if node.left is not None:
        backTrack(node.left, ret, array)
        array.pop(len(array)-1)

    if node.right is not None:
        backTrack(node.right, ret, array)
        array.pop(len(array) - 1)

    ret.append(copy.deepcopy(array))


def solution(array):
    t = Tree()
    for i in array:
        t.pushNode(i)

    # t.printPreOrder()
    printArray = []

    backTrack(t.root, printArray, [])
    print(printArray)




solution([3, 5, 1, 2, 6, 4])

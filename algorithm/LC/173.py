class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class tree:
    root = None

    def insert(self, node, c):
        if node is None:
            node = Node(c)
        else:
            if node.data < c:
                node.right = self.insert(node.right, c)
            else:
                node.left = self.insert(node.left, c)
        return node

    def insertNode(self, c):
        self.root = self.insert(self.root, c)

    def inOrder(self, node, array):
        if node.left is not None:
            self.inOrder(node.left, array)
        array.append(node.data)
        if node.right is not None:
            self.inOrder(node.right, array)

    def inOrderTree(self):
        returnArray = []
        self.inOrder(self.root, returnArray)
        return returnArray

    def preOrder(self, node, array):
        array.append(node.data)

        if node.left is not None:
            self.preOrder(node.left, array)
        if node.right is not None:
            self.preOrder(node.right, array)

    def preOrderTree(self):
        returnArray = []
        self.preOrder(self.root, returnArray)
        return returnArray

    def postOrder(self, node, array):
        if node.left is not None:
            self.postOrder(node.left, array)

        if node.right is not None:
            self.postOrder(node.right, array)

        array.append(node.data)

    def postOrderTree(self):
        returnArray = []
        self.postOrder(self.root, returnArray)
        return returnArray

def solution(array):
    t = tree()

    for i in array:
        t.insertNode(i)

    print(t.inOrderTree())
    print(t.preOrderTree())
    print(t.postOrderTree())

# solution([6,3,1,4,2,8,9,0])
solution(['F', 'B', 'A', 'D', 'E', 'C', 'G', 'I', 'H'])

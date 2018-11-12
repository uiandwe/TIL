class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class link:
    root = None
    firstNode = None
    lastNode = None


    def insert(self, node, val):
        if node is None:
            return Node(val)
        else:
            node.next = self.insert(node.next, val)
            return node

    def insertNode(self, val):
        self.root = self.insert(self.root, val)

    def getNode(self, node, val):
        if node is None:
            return False
        else:
            if node.data == val:
                return True
            else:
                return self.getNode(node.next, val)

    def findVal(self, val):
        return self.getNode(self.root, val)


def solution(array):
    l = link()

    for i in array:
        l.insertNode(i)

    print(l.findVal(1))
    print(l.findVal(6))


print(solution([1, 2, 3, 4]))

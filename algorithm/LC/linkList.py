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

    def delNode(self, node, preNode, val):
        if node is None:
            return False
        else:
            if node.data == val:
                if preNode is None: #첫번째 노드라면
                    self.root = node.next
                else:
                    preNode.next = node.next
                node = None
                return True
            else:
                return self.delNode(node, node.next, val)

    def removeNode(self, val):
        return self.delNode(self.root, None, val)

    def pNode(self, node):
        if node is not None:
            print(node.data)
            self.pNode(node.next)

    def printNode(self):
        self.pNode(self.root)


def solution(array):
    l = link()

    for i in array:
        l.insertNode(i)

    print(l.findVal(1))
    print(l.findVal(6))

    l.removeNode(1)

    l.printNode()


print(solution([1, 2, 3, 4]))

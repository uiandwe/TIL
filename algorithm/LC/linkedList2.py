class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        first = Node("")
        self.head = first
        self.tail = first

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def allNode(self, node, array):
        if node is not None:
            array.append(node.data)
            self.allNode(node.next, array)

    def allNodeArray(self):
        returnArray = []
        self.allNode(self.head, returnArray)
        return returnArray


def solution(array):
    l = LinkedList()

    for i in array:
        l.append(i)
        
    print(l.allNodeArray())

solution(['a', 'b', 'c', 'd'])

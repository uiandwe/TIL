class Node:
    start = None
    end = None

    def insert(self, data):
        n = Node()
        n.data = data
        n.next = None
        if self.end is not None:
            self.end.next = n
            self.end = n
        else:
            self.end = self.start = n

    def insertArray(self, array):
        for i in array:
            self.insert(i)

    def printNode(self):
        n = self.start
        array = []
        while n is not None:
            array.append(n.data)
            n = n.next

        return array

def mergeLinkList(link1, link2):
    point1 = link1.start
    point2 = link2.start
    temp = []
    while point1 is not None or point2 is not None:
        if point1 is None or (point2 is not None and point1.data >= point2.data):
            temp.append(point2.data)
            point2 = point2.next
        elif point2 is None or (point1 is not None and point1.data <= point2.data):
            temp.append(point1.data)
            point1 = point1.next

    return temp



def solution(array1, array2):
    print(array1, array2)
    n1 = Node()
    n1.insertArray(array1)

    n2 = Node()
    n2.insertArray(array2)

    print(mergeLinkList(n1, n2))

solution([1, 2, 4], [1, 3, 4])

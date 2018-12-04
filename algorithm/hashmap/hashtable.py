class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class HashTable:
    def __init__(self):
        self.dict = {}

    def hash(self, str):
        c = 0
        for i in str:
            c += ord(i)

        return c%10

    def input(self, k, v):
        if k in self.dict:
            node = self.dict[k]
            while node.next is not None:
                node = node.next
            n = Node(v)
            node.next = n
        else:
            self.dict[k] = Node(v)

    def getValue(self, v):
        k = self.hash(v)
        if k in self.dict:
            node = self.dict[k]
            while node is not None:
                if node.data == v:
                    return node.data
                elif node.next is None:
                    return -1
                else:
                    node = node.next
        else:
            return -1

ht = HashTable()

ht.input(ht.hash("a"), "a")
ht.input(ht.hash("b"), "b")
ht.input(ht.hash("c"), "c")
ht.input(ht.hash("k"), "k")
print(ht.dict[7], ht.dict[7].next, ht.dict[7].next.data)
print(ht.getValue("k"), ht.getValue("d"))

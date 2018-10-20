from Node import Node

class BinarySearchTree(object):
    root = None

    def __init__(self):
        self.root = None

    def insertValue(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insertValue(node.left, data)
            else:
                node.right = self.insertValue(node.right, data)
        return node

    def insert(self, data):
        self.root = self.insertValue(self.root, data)
        return self.root is not None

    def find(self, key):
        return self.findValue(self.root, key)

    def findValue(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.findValue(root.left, key)
        else:
            return self.findValue(root.right, key)

    def delete(self, key):
        self.root, deleted = self.deleteValue(self.root, key)
        return deleted

    def deleteValue(self, node, key):
        if node is None:
            return node, False

        deleted = False

        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self.deleteValue(node.left, key)
        else:
            node.right, deleted = self.deleteValue(node.right, key)
        return node, deleted

    def preOrder(self, node):
        if node.left is not None:
            self.preOrder(node.left)

        print node.data

        if node.right is not None:
            self.preOrder(node.right)

    def inOrder(self, node):
        print node.data

        if node.left is not None:
            self.inOrder(node.left)

        if node.right is not None:
            self.inOrder(node.right)

    def postOrder(self, node):
        if node.left is not None:
            self.postOrder(node.left)

        if node.right is not None:
            self.postOrder(node.right)

        print node.data

    def getDepth(self):
        pass


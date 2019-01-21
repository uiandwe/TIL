class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, node, data):
        if node is None:
            node = TreeNode(data)
        else:
            if node.val > data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)

        return node

    def insertArr(self, arr, root):
        for i in range(1, len(arr)):
            root = self.insert(root, arr[i])

        return root

    def rangeSumBST(self, node, left, right):
        if node is None:
            return 0
        if node.val < left:
            return self.rangeSumBST(node.right, left, right)
        elif node.val > right:
            return self.rangeSumBST(node.left, left, right)
        else:
            return self.rangeSumBST(node.left, left, right) +\
                   node.val + self.rangeSumBST(node.right, left, right)


def solution(arr, left, right):
    root = TreeNode(arr[0])
    root = root.insertArr(arr, root)

    return root.rangeSumBST(root, left, right)


if __name__ == "__main__":
    solution([10, 5, 15, 3, 7, 18], 7, 15)

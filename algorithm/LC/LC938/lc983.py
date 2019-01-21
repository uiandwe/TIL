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

    def preOrderSearchNode(self, node, val):

        if node.val == val:
            return node

        if node.left is not None:
            temp_node = self.preOrderSearchNode(node.left, val)
            if temp_node is not None:
                return temp_node

        if node.right is not None:
            temp_node = self.preOrderSearchNode(node.right, val)
            if temp_node is not None:
                return temp_node

    def betweenSum(self, node, left, right, retArr):
        if node is not None:
            if left < node.val and right > node.val:
                retArr.append(node.val)

            if node.left is not None:
                self.betweenSum(node.left, left, right, retArr)

            if node.right is not None:
                self.betweenSum(node.right, left, right, retArr)


def solution(arr, left, right):
    root = TreeNode(arr[0])
    root = root.insertArr(arr, root)

    betweenArr = []
    root.betweenSum(root, left, right, betweenArr)

    search_left_node = root.preOrderSearchNode(root, left)
    root.betweenSum(search_left_node.right, left, right, betweenArr)

    search_right_node = root.preOrderSearchNode(root, right)
    root.betweenSum(search_right_node.left, left, right, betweenArr)

    return left + sum(list(set(betweenArr))) + right


if __name__ == "__main__":
    solution([10, 5, 15, 3, 7, 18], 7, 15)

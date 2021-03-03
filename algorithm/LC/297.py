# -*- coding: utf-8 -*-
from collections import deque


class Codec:

    def serialize(self, root):
        if root is None:
            return ''
        q = deque([root])
        l = []
        while q:
            n = q.popleft()
            if n is not None:
                q.append(n.left)
                q.append(n.right)
                l.append(str(n.val))
            else:
                l.append('Null')
        return ' '.join(l)

    def deserialize(self, data):
        if data == '': return None
        array = data.split(' ')
        root = TreeNode(int(array[0]))
        q = deque([root])
        index = 1
        while q:
            n = q.popleft()
            if array[index] != 'Null':
                n.left = TreeNode(int(array[index]))
                q.append(n.left)
            index += 1
            if array[index] != 'Null':
                n.right = TreeNode(int(array[index]))
                q.append(n.right)
            index += 1
        return root

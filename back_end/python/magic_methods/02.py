# -*- coding: utf-8 -*-
class Node:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val

if __name__ == '__main__':

    n1 = Node(10)
    n2 = Node(20)

    if n1 == n2:
        print("equal True")
    else:
        print("equal False")

    if n1 != n2:
        print("not equal True")
    else:
        print("not equal False")

    if n1 < n2:
        print("lt True")
    else:
        print("lt False")

    if n1 > n2:
        print("gt True")
    else:
        print("gt False")

    if n1 <= n2:
        print("le True")
    else:
        print("le False")

    if n1 >= n2:
        print("ge True")
    else:
        print("ge False")

# -*- coding: utf-8 -*-
import math

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

    def __pos__(self):
        return self.val + 1

    def __neg__(self):
        return self.val - 1

    def __abs__(self):
        return abs((self.val*-1))

    def __add__(self, other):
        return self.val + other.val

    def __sub__(self, other):
        return self.val - other.val

    def __mul__(self, other):
        return self.val * other.val

    def __floordiv__(self, other):
        return self.val // other.val

    def __truediv__(self, other):
        return self.val / other.val

    def __mod__(self, other):
        return self.val % other.val

    def __pow__(self, power, modulo=None):
        return self.val ** power

    def __invert__(self):
        return ~self.val

    def __round__(self):
        return float(self.val)

    def __floor__(self):
        return float(self.val)

    def __lshift__(self, other):
        return self.val << 1

    def __rshift__(self, other):
        return self.val >> 1

    def __and__(self, other):
        return self.val & other.val

    def __or__(self, other):
        return self.val | other.val


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


    print("__pos__", +n1)
    print("__neg__", -n1)
    print("__abs__", abs(n1))
    print("add ", n1 + n2)
    print("sub ", n1 - n2)
    print('mul', n1 * n2)
    print('truediv', n1 / n2)
    print("floordiv ", n1.__floordiv__(n2))
    print('mod', n1 % n2)

    print("pow", pow(n1, 2))

    print("invert", ~n1)
    print("round", round(n1))
    print("floor", math.floor(n1))


    print("lsift", n1 << 1)
    print("rsift", n1 >> 1)


    print("and", n1 & n2)
    print("or", n1 | n2)

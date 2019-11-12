# -*- coding: utf-8 -*-
import os


class MagicMethod:
    '''docstring'''

    # def __new__(cls, *args, **kwargs):
    #     if len(args) < 1:
    #         return None
    #     else:
    #         return super(MagicMethod, cls).__new__(cls)

    def __init__(self):
        print("__init__")

    def __del__(self):
        print("__del__")

    def __call__(self, *args, **kwargs):
        print("__call__")
        return None

    def __eq__(self, other):
        if self.__class__ == other:
            return True

if __name__ == '__main__':
    mm = MagicMethod()
    mm()
    if mm == MagicMethod:
        print("eq pass")

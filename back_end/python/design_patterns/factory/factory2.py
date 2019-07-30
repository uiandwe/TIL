# -*- coding: utf-8 -*-
import sys
import abc

class BaseOperator:
    @abc.abstractmethod
    def execute(self):
        print("BaseOperator execute")

class gfsOperator(BaseOperator):
    def execute(self):
        print("gfsOperator execute")

class kmipaOperator(BaseOperator):
    def execute(self):
        print("kmipaOperator execute")


DICT_OPS = {
    'gfs': gfsOperator,
    'kmipa': kmipaOperator
}


def factory_method(cmd):
    factory = DICT_OPS.get(cmd, BaseOperator)
    return factory


if __name__ == '__main__':
    args = sys.argv[1:]
    app = factory_method(*args)
    app.execute(app)

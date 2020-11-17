# -*- coding: utf-8 -*-
import copy


class Hello:
    def __init__(self, msg):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, msg):
        self._msg = msg


h = Hello("헬")
h2 = copy.deepcopy(h) # prototype 패턴
print(h.msg, h2.msg)
h2.msg = "hell"
print(h.msg, h2.msg)

# -*- coding: utf-8 -*-
import abc


class ByteSource(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        raise NotImplementedError

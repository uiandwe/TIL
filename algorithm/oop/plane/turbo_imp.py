# -*- coding: utf-8 -*-
import abc


class TurboImp(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def boost(self):
        raise NotImplementedError()

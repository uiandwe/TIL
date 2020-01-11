# -*- coding: utf-8 -*-
import abc


class StealthImp(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start_stealth(self):
        raise NotImplementedError

    @abc.abstractmethod
    def stop_stealth(self):
        raise NotImplementedError

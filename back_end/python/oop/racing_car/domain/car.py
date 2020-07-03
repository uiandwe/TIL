# -*- coding: utf-8 -*-


class Car:

    error_name_max_length_message = '이름은 5자 이하'

    def __init__(self, name):
        self.valid_name(name)
        self.name = name
        self.engine = None
        self.distance = 0

    def set_engine(self, engine):
        self.engine = engine

    def valid_name(self, name):
        if len(name) > 5:
            raise Exception(self.error_name_max_length_message)

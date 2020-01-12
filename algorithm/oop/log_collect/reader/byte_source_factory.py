# -*- coding: utf-8 -*-
from oop.log_collect.singleton import Singleton
from oop.log_collect.reader.file_data_reader import FileDataReader
from oop.log_collect.reader.socket_data_reader import SocketDataReader
from oop.log_collect.reader.db_data_reader import DbDataReader


class ByteSourceFactory(metaclass=Singleton):

    def __init__(self, type):
        self.type = type

    def __call__(self, *args, **kwargs):
        if self.type == 'file':
            source = FileDataReader()
        elif self.type == 'socket':
            source = SocketDataReader()
        else:
            source = DbDataReader()

        return source.read()

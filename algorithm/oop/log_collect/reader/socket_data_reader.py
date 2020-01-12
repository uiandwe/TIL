# -*- coding: utf-8 -*-
from oop.log_collect.reader.byte_source import ByteSource


class SocketDataReader(ByteSource):

    def read(self):
        print("SocketDataReader read")
        return "SocketDataReader read"

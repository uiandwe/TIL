# -*- coding: utf-8 -*-
from oop.log_collect.reader.byte_source import ByteSource


class DbDataReader(ByteSource):

    def read(self):
        print("DbDataReader read")
        return "DbDataReader read"

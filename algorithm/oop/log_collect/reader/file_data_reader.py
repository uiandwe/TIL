# -*- coding: utf-8 -*-
from oop.log_collect.reader.byte_source import ByteSource


class FileDataReader(ByteSource):

    def read(self):
        print("FileDataReader read")
        return "FileDataReader read"

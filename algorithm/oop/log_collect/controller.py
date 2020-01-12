# -*- coding: utf-8 -*-

from oop.log_collect.writer.file_data_writer import FileDataWriter
from oop.log_collect.encryptor.encryptor import Encryptor
from oop.log_collect.reader.byte_source_factory import ByteSourceFactory


class LogController:

    def __init__(self, reader_type):
        self.reader_type = reader_type

    def process(self):
        source = ByteSourceFactory(self.reader_type)
        data = source()

        encryptor = Encryptor()
        encrypted_data = encryptor.encrypt(data)

        writer = FileDataWriter()
        writer.write(encrypted_data)


if __name__ == '__main__':
    log_controller = LogController('db')
    log_controller.process()

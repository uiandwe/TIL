# -*- coding: utf-8 -*-
# 팩토리는 같은것을 찍어내느게 아닌(같은것은 싱글톤)
# 산출물은 상위단이 어떻게 동작하는지 알필요 없을때 (class에 따라서 분기가 되지만 그상위단이 어떤것을 상속받는지 알필요 없을때) 사용한다.
# 상속을 통해 abstractmethod로 만들어진 함수를 구현합으로서 
# 하위단은 같은 기능을 그냥 사용할뿐 상위단은 알필요가 없다.(http / ftp든 같은 connect / get_response를 사용한다.)
import abc


class Connector():
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def get_response(self):
        pass


class HTTPConnection(Connector):
    def __init__(self):
        self.protocol = 'http'

    def connect(self):
        return self.protocol + " connected"

    def get_response(self):
        return "http listen"


class FTPConnection(Connector):
    def __init__(self):
        self.protocol = 'ftp'

    def connect(self):
        return self.protocol + " connected"

    def get_response(self):
        return "ftp listen"


class SimpleFactory(object):

    @staticmethod
    def build_connetion(protocol):
        if protocol == 'http':
            return HTTPConnection()
        elif protocol == 'ftp':
            return FTPConnection()
        else:
            raise RuntimeError("unknown protocol")


if __name__ == '__main__':
    protocol = input(':')
    protocol = SimpleFactory.build_connetion(protocol)
    protocol.connect()
    print(protocol.get_response())

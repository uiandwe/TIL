# -*- coding: utf-8 -*-
import time

class Subject(object):
    def __init__(self):
        self.observers = []
        self.cur_time = None

    def register_observer(self, observer):
        if observer in self.observers:
            print('already in observer')
        else:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('no search observer')

    def notify(self):
        self.cur_time = time.time()
        for observer in self.observers:
            observer.notify(self.cur_time)


from abc import ABCMeta, abstractmethod
import datetime
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self, unix_timestamp):
        pass


class USATimeObserber(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-d %I:%M:%S%p')
        print('observer', self.name, time)


class EUTimeObserber(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-d %H:%M:%S')
        print('observer', self.name, time)


if __name__ == '__main__':
    subject = Subject()

    observer1 = USATimeObserber('usa')
    subject.register_observer(observer1)
    subject.notify()

    observer2 = EUTimeObserber('eu')
    subject.register_observer(observer2)
    subject.notify()

    time.sleep(2)
    print('remove use')
    subject.unregister_observer(observer1)
    subject.notify()



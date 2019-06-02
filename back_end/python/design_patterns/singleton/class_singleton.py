# -*- coding: utf-8 -*-
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance



if __name__ == '__main__':
    singleton = Singleton()
    another_singleton = Singleton()
    print(singleton is another_singleton)

    singleton.only_one_var = "I'm only one var"
    print(another_singleton.only_one_var)


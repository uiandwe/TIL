# -*- coding: utf-8 -*-
# 
# 상속시 각 객체의 정보를 따로 가지고 싶다면 borg 싱글톤을 이용
# 모두 같은 속성을 하나만 사용한다면 클래식 싱글톤을 사용

class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class Child(Borg):
    pass


if __name__ == '__main__':
    borg = Borg()
    another_singleton = Borg()
    print(borg is another_singleton)

    borg.only_one_var = "I'm only one var"
    print(another_singleton.only_one_var)

    child = Child()
    print(child is borg)
    print(child.only_one_var)

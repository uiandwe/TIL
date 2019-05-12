# -*- coding: utf-8 -*-

class Department():
    def __init__(self, name):
        self.name = name
        self.manager = name

    def getManager(self):
        return self.manager

class Person():
    def __init__(self):
        self._department = None

    def getDepartment(self):
        return self._department

    def setDepartment(self, name):
        self._department = Department(name)


class Person1():
    def __init__(self):
        self._department = None

    def getDepartment(self):
        return self._department.getManager()

    def setDepartment(self, name):
        self._department = Department(name)


if __name__ == '__main__':
    john = Person()
    john.setDepartment("before 개발")
    # 객체안의 변수에서 다시 호출하여 메소드 체인에 의한 호출이됨 (연속적으로 불리여서 어떤 객체인지 알수 없음)
    manager = john.getDepartment().getManager()

    print(manager)


    john = Person1()
    john.setDepartment("after 개발")
    # 한번에 불러올수 있도록 클래스 수정
    manager = john.getDepartment()

    print(manager)

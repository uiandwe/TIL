# -*- coding: utf-8 -*-
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

mc = MyClass()



class validatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('polygons need 3+')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=validatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides -2) * 180

class Triangle(Polygon):
    sides = 3


print('before')
t = Triangle()

# sides 가 3 이하로 선언시 에러가 발생
# 상위 클래스에서 강제로 상속의 변수를 통해 제어 
class Line(Polygon):
    print('before sides')
    sides = 1
    print('after sides')

print('after class')


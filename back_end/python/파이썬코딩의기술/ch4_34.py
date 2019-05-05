# -*- coding: utf-8 -*-
import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})

#직렬화 하기
class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point@d(%d, %d)' % (self.x, self.y)


point = Point2D(5, 3)
print('object ', point)
print(point.serialize())

print("=======================================")

# 더 좋은 방법으로 역직렬화 하기
class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])


class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point@d(%d, %d)' % (self.x, self.y)


point = BetterPoint2D(5, 3)
print('Before ', point)
data = point.serialize()
print('Seralize ', data)
after = BetterPoint2D.deserialize(data)
print('after ', after)


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
        })

    def __repr__(self):
        return 'BetterSerializable' + self.args

print("=========================================")

registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class BetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point@d(%d, %d)' % (self.x, self.y)

# 함수를 따로 호출해줘야 한다. 불편~
register_class(BetterSerializable)

point = BetterPoint2D(5, 3)
print(point)
data = point.serialize()
print('serialized ', data)
# after = deserialize(data)
# print(after)


print("=========================================")

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

# meta를 통해 미들웨어를 만들 수 있다!!
class RegisterdSerializeable(BetterSerializable, metaclass=Meta):
    pass
    

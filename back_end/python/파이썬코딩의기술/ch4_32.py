# -*- coding: utf-8 -*-
class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = 'Value for %s' % item
        setattr(self, item, value)
        return value

data = LazyDB()
print('before ', data.__dict__)
print('foo ', data.foo)
print('after ', data.__dict__)


# __getattr__은 객체의 인스턴스 딕셔너리에 접근 할때만 호출
# __getattribute__은 객체의 속성에 접근 할때마다 호출

print("---------------------------------")

class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print('called __getattribute__(%s) ' % item )
        try:
            return super().__getattribute__(item)
        except AttributeError:
            value = 'Value for %s' % item
            setattr(self, item, value)
            return value


data1 = ValidatingDB()
print('before ', data1.exists)
print('foo ', data1.foo)
print('after ', data1.foo)


print("---------------------------------")

# 객체에 접근할때마다 getattribute / setattr 이 호출됨
class SavingDB(object):
    def __setattr__(self, key, value):
        super().__setattr__(key, value)

class LogginSavingDB(SavingDB):
    def __setattr__(self, key, value):
        print('called __setattr__ (%s, %r)' % (key, value))
        super().__setattr__(key, value)

data = LogginSavingDB()
print('before ', data.__dict__)
data.foo = 5
print('after1 ', data.__dict__)
data.foo = 7
print('after2 ', data.__dict__)


print("---------------------------------")
# __getattribute__에서 데이터 참조시 self.* 에 접근할경우 객체를 참조했으므로 다시 __getattribue를 참조, 재귀호출이 되버린다. 
# super로 가져와서 참조하면 됨
class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        print('Called __getattribute__(%s)' % item)
        data_dict = super().__getattribute__('_data')
        return data_dict[item]
        # return self._data[item]


data = BrokenDictionaryDB({'foo': 3})
print(data.foo)

# -*- coding: utf-8 -*-


class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print("before : ", r0.get_ohms())
r0.set_ohms(10e3)
print("after : ", r0.get_ohms())

# 증가 시킬땐 불편함
r0.set_ohms(r0.get_ohms() + 5e03)


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3
# 굳이 셋터겟터는 쓰지 말자
r1.ohms += 5e3


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        print("pass volteage1")
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        print("pass volteage2")
        self._voltage = voltage
        self.current = self._voltage / self.ohms

# @setter을 통해 값을 넣을때 검증 및 업데이트를 할수 있다.
r2 = VoltageResistance(1e3)
print("before : ", r2.current)
r2.voltage = 10
print("after : ", r2.current)


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(ohms)
        self._ohms = ohms


r3 = BoundedResistance(1e3)
# 잘못된 값을 넣으면 에러 발생 (valid)
# r3.ohms = 0
# 생성자에도 잘못된 값을 넣으면 에러 (valid)
# BoundedResistance(-1)

class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("can't set attribute")
        self._ohms = ohms

r4 = FixedResistance(1e3)
# 이미 값이 있기 때문에 에러 발생 
r4.ohms = 2e3

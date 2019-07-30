# -*- coding: utf-8 -*-
class Celsius:
    def __init__(self):
        pass

    @property
    def temperature(self):
        print("getting value")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("not possible")
        print("setting value")
        self.__temperature = value


if __name__ == '__main__':
    c = Celsius()
    c.temperature = 100
    print(c.temperature)
    
    c.temperature = -300

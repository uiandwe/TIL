class Audience:
    def __init__(self, bag):
        self.__bag = bag

    @property
    def bag(self):
        return self.__bag
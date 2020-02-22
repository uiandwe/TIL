class Invitation:
    def __init__(self, date):
        self.__when = date

    @property
    def when(self):
        return self.__when

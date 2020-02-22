class Ticket:
    def __init__(self, fee):
        self.__fee = fee

    @property
    def fee(self):
        return self.__fee

class TicketOffice:
    def __init__(self, amount, tickets):
        self.__amount = amount
        self.__tickets = tickets

    @property
    def tickets(self):
        return self.__tickets.pop(0)

    def minus_amount(self, amount):
        self.__amount -= amount

    def plus_amount(self, amount):
        self.__amount += amount
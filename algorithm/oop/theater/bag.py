class Bag:
    def __init__(self, amount, invitation=None):
        self.__amount = amount
        self.__invitation = invitation
        self.__ticket = None

    def has_invitation(self):
        return self.__invitation is None

    def has_ticket(self):
        return self.__ticket is None

    @property
    def ticket(self):
        return self.__ticket

    @ticket.setter
    def set_ticket(self, ticket):
        self.__ticket = ticket

    def minus_amount(self, amount):
        self.__amount -= amount

    def plus_amount(self, amount):
        self.__amount += amount


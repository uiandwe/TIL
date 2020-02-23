class Audience:
    def __init__(self, bag):
        self.__bag = bag

    def buy(self, ticket):
        if self.__bag.has_invitation():
            self.__bag.set_ticket(ticket)
            return 0
        else:
            self.__bag.set_ticket(ticket)
            self.__bag.minus_amount(ticket.fee())
            return ticket.fee()

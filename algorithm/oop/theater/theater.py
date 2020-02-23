class Theater:
    def __init__(self, ticket_seller):
        self.__ticket_seller = ticket_seller

    def enter(self, audience):
        self.__ticket_seller.sell_t(audience)
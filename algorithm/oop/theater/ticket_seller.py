class TicketSeller:
    def __init__(self, ticket_office):
        self.__ticket_office = ticket_office

    def sell_to(self, audience):
        self.__ticket_office.plus_amount(audience.buy(self.__ticket_office.tickets()))

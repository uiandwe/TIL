class TicketSeller:
    def __init__(self, ticket_office):
        self.__ticket_office = ticket_office

    @property
    def ticket_office(self):
        return self.__ticket_office

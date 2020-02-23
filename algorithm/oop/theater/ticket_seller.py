class TicketSeller:
    def __init__(self, ticket_office):
        self.__ticket_office = ticket_office

    def sell_to(self, audience):
        if audience.bag().has_invitation():
            ticket = self.__ticket_office.ticket()
            audience.bag().set_ticket(ticket)

        else:
            ticket = self.__ticket_office.ticket()
            audience.bag().miuns_amount(ticket.fee())
            self.__ticket_office.plus_amount(ticket.fee())
            audience.bag().set_ticket(ticket)

class Theater:
    def __init__(self, ticket_seller):
        self.__ticket_seller = ticket_seller

    def enter(self, audience):
        if audience.bag().has_invitation():
            ticket = self.__ticket_seller.ticket_office().ticket()
            audience.bag().set_ticket(ticket)

        else:
            ticket = self.__ticket_seller.ticket_office().ticket()
            audience.bag().miuns_amount(ticket.fee())
            self.__ticket_seller.ticket_office().plus_amount(ticket.fee())
            audience.bag().set_ticket(ticket)

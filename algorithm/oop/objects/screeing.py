# -*- coding: utf-8 -*-
from .reservation import Reservation


class Screeing:

    def __init__(self, movie, sequence, when_screened):
        self.movie = movie
        self.sequence = sequence
        self.when_screened = when_screened

    def get_start_time(self):
        return self.when_screened

    def is_sequence(self, sequence):
        return self.sequence == sequence

    def get_movie_fee(self):
        return self.movie.get_fee()

    def calculate_fee(self, audience_count):
        return self.movie.calculate_movie_fee().times(audience_count)

    def reserve(self, customer, audience_count):
        return Reservation(customer, self.calculate_fee(audience_count), audience_count)



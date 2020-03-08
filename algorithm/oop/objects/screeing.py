# -*- coding: utf-8 -*-
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

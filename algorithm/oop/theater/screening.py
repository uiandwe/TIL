class Screening:
    def __init__(self, movie, sequence):
        self.movie = movie
        self.sequence = sequence

    def is_sequence(self, sequence):
        return self.sequence == sequence

    def get_movie_fee(self):
        return self.movie.get_fee()


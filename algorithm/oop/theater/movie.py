class Movie:
    def __init__(self, title, running_time, fee, discount_policy):
        self.title = title
        self.running_time = running_time
        self.fee = fee
        self.discount_policy = discount_policy

    def get_fee(self):
        return self.fee

    def calculate_movie_fee(self, screening):
        return self.fee - self.discount_policy.calculate_discount_amount(screening)
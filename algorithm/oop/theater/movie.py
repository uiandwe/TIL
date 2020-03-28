class Movie:
    def __init__(self, title, running_time, fee):
        self.title = title
        self.running_time = running_time
        self.fee = fee

    def get_fee(self):
        return self.fee
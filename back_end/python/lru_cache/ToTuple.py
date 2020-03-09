class ToTuple:
    def __init__(self):
        self.l = []

    def dictionary_check(self, input):
        for key, value in input.items():
            if isinstance(value, dict):
                self.dictionary_check(value)
                self.l.append(key)
            elif isinstance(value, list):
                self.list_check(value)
                self.l.append(key)
            else:
                self.l.append(key)
                self.l.append(value)

    def list_check(self, input):
        for value in input:
            if isinstance(value, list):
                self.list_check(value)
            elif isinstance(value, dict):
                self.dictionary_check(value)
            else:
                self.l.append(value)

    def __call__(self, values):
        self.l = []
        if isinstance(values, dict):
            self.dictionary_check(values)
        else:
            self.list_check(values)

    def __hash__(self):
        return hash(tuple(self.l))




th = ToTuple()
th({"test": 1, "test2": 2, "1111": { "123" : [1, 2, {"ppp": 55}]}})
print(th.__hash__())
th({"test": 1, "test2": 2, "1111": { "123" : [1, 2, {"ppp": 55}]}})
print(th.__hash__())

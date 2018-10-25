class acm11732:
    d = 0

    def add(self, x):
        self.d = bin(int(self.d, 2) + x)

    def remove(self, x):
        self.d = bin(int(self.d, 2) - x)

    def check(self, x):
        if  int(self.d, 2) & x > 0:
            return True
        else:
            return False

    def toggle(self, x):
        pass

    def all(self):
        self.d = bin(20)

    def empty(self):
        self.d = bin(0)


a = acm11732()

print a.d
a.all()
print a.d
a.empty()
print a.d
a.add(10)
print a.d
a.remove(2)
print a.d
print a.check(8)
print a.check(3)
print a.check(1)
a.add(2)
print a.d
print a.check(8)
print


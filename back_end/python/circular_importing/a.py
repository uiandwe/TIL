from b import B

class A:
    def __init__(self, params=0):
        print("init A ", params)

    def test(self):
        B()
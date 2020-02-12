import importlib

class B:
    def __init__(self):
        a = importlib.import_module('a')
        a.A()

        import a
        a.A()

        a = __import__("a")
        a.A()
        print("init B")
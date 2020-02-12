import importlib

class B:
    def __init__(self):
        a = importlib.import_module('a')
        a.A("1")

        import a
        a.A("2")

        a = __import__("a")
        a.A("3")

        getattr(__import__('a'), 'A')("4")


        print("init B")
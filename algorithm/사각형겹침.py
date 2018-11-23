class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        width = self.w
        height = self.h
        return width * height

    def getIntersection(self, r1, r2):

        if r1.x > r2.x + r2.w:
            return False
        if r1.x + r1.w < r2.x:
            return False
        if r1.y > r2.y + r2.h:
            return False
        if r1.y + r1.h < r2.y:
            return False

        x = max(r1.x, r2.x)
        y = max(r1.y, r2.y)
        w = min(r1.x + r1.w, r2.x + r2.w) - x
        h = min(r1.y + r1.h, r2.y + r2.h) - y

        rect = Rect(x, y, w, h)
        return rect



def solution():
    r1 = Rect(0, 0, 100, 100)
    r2 = Rect(50, 50, 50, 50)
    r3 = Rect(50, 0, 50, 50)

    g1 = r1.getIntersection(r1, r2)
    g2 = r1.getIntersection(r1, r3)
    print(r1.area(), r1.area() - g1.area() - g2.area())

solution()

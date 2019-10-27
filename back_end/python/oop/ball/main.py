# -*- coding: utf-8 -*-
import turtle
from ball import Ball
from block import Block


class Main:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("ball simulator")
        self.wn.tracer(0)

        self.balls = []

        for _ in range(25):
            b = Ball(turtle.Turtle())
            self.balls.append(b)

        # block = Block(turtle.Turtle())

    def __call__(self, *args, **kwargs):
        while True:
            self.wn.update()
            for ball in self.balls:
                ball.move()
        self.wn.mainloop()


if __name__ == '__main__':
    m = Main()
    m()

# -*- coding: utf-8 -*-
import random


class Block:
    def __init__(self, b):
        self.block = b
        self.block.shape("square")
        self.block.color("white")
        self.block.penup()
        self.block.speed(0)

        x = random.randint(-290, 290)
        y = random.randint(200, 400)

        self.block.goto(x, y)

        print(dir(self.block))
        print(self.block.xcor(), self.block.ycor())
        print(self.block.width(), self.block.height())

# -*- coding: utf-8 -*-
import random


class Ball:

    def __init__(self, b):
        colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
        self.ball = b
        self.ball.shape("circle")
        self.ball.color(random.choices(colors))
        self.ball.penup()
        self.ball.speed(0)

        x = random.randint(-290, 290)
        y = random.randint(200, 400)

        self.ball.goto(x, y)
        self.ball.dy = 0
        self.ball.dx = random.randint(-3, 3)
        self.ball.da = random.randint(-5, 3)

    def move(self):
        gravity = 0.1

        self.ball.rt(self.ball.da)
        self.ball.dy -= gravity
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        self.ball.setx(self.ball.xcor() + self.ball.dx)

        # wall check
        if self.ball.xcor() > 300:
            self.ball.dx *= -1

        if self.ball.xcor() < -300:
            self.ball.dx *= -1

        # bounce
        if self.ball.ycor() < -300:
            self.ball.sety(-300)
            self.ball.dy *= -1

    def crash(self):
        pass

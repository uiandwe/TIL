# -*- coding: utf-8 -*-
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("ball simulator")
wn.tracer(0)

balls = []

for _ in range(25):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]


for ball in balls:
    ball.shape("circle")
    ball.color(random.choices(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 3)


gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # wall check
        if ball.xcor() > 300:
            ball.dx *= -1

        if ball.xcor() < -300:
            ball.dx *= -1

        # bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1


wn.mainloop()

# -*- coding: utf-8 -*-
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("ball simulator")
wn.tracer(0)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = 0
ball.dx = 2


gravity = 0.1

while True:
    wn.update()
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
        ball.dy *= -1


wn.mainloop()

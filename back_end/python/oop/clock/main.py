# -*- coding: utf-8 -*-

import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("시발")


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)


    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)


    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

draw_clock(pen)
wn.mainloop()

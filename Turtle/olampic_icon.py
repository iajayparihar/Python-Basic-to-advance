from turtle import *

def cir(clr,rad,x,y):
    penup()
    setpos(x,y)
    color(clr)
    pendown()
    circle(rad)
pensize(3)
cir("yellow", 51, -100, -25)
cir("blue", 51,    10, -25)
cir("black", 51,   120, -25)
cir("green", 51,  -45, -75)
cir("orange", 51, 45, -75)

turtle.done()
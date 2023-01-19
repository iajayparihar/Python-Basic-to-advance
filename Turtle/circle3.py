from turtle import *
import time as t

speed(0)
pensize(3)
radius=100
color("red","green")
begin_fill()
circle(radius)
end_fill()

color("green",'red')
begin_fill()
circle(-radius)
end_fill()

def inside_circle(rad,ang):
    angle=150
    color("yellow","pink")
    begin_fill()
    circle(rad,ang)
    end_fill()
    penup()
    home()
    pendown()

inside_circle(40,150)
inside_circle(40,-150)
inside_circle(-40,150)
inside_circle(-40,-150)
done()
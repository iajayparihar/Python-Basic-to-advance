from turtle import *
hideturtle()
scr=Screen()
t=Turtle()
speed(0)
def semi_circle(clr,rad,val):
    t.color(clr)
    t.circle(rad,-180)
    t.up()
    t.setpos(val,0)
    t.down()
    t.right(180)

clr=["violet","indigo","blue","green","yellow","orange","red"]

scr.setup(800,600)
scr.bgcolor("black")
t.right(90)
t.width(11)

for i in range(7):
    semi_circle(clr[i],10*(i+10), -10*(i+1))
    
done()
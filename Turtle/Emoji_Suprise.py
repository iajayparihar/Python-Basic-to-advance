import turtle
t= turtle.Turtle()
t.speed(9)
t.begin_fill()
t.color("yellow")
t.circle(100)
t.end_fill()
# right eye
t.up()
t.setpos(-35,105)
t.begin_fill()
t.color("black")
t.circle(25)
t.end_fill()
#right eye dot
t.begin_fill()
t.color("white")
t.circle(15)
t.end_fill()

# left eye
t.up()
t.setpos(35,105)
t.begin_fill()
t.color("black")
t.circle(25)
t.end_fill()
#left eye dot
t.begin_fill()
t.color("white")
t.circle(15)
t.end_fill()


# mouth
t.up()
t.setpos(0,25)
t.begin_fill()
t.color("black")
t.circle(25)
t.end_fill()

turtle.done()
import turtle

t= turtle.Turtle()
t.color("red")
t.begin_fill()
t.up()
t.forward(100)
t.down()
for i in range(4):
    t.forward(100)
    t.right(90)
# t.up()
t.end_fill()
turtle.done()

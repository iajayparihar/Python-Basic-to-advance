import turtle

colors =['red','purple','blue','green','orange','yellow']
t = turtle.Pen() # capital P in Pen remember
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()
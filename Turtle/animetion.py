import turtle

def move_obj(ball):
    ball.fillcolor("yellow")
    ball.begin_fill()
    ball.circle(25)
    ball.end_fill()

scr=turtle.Screen()
ball=turtle.Turtle()
scr.setup(650,650) # APPERed screen size
scr.bgcolor("light green")
scr.tracer(0)

ball.color("red")
ball.width(2)
ball.hideturtle()
ball.penup()
ball.goto(-350,0)
ball.pendown()
i=0
while i<=5000:
    ball.clear()
    move_obj(ball)
    scr.update()
    ball.forward(0.5)
    ball.write("Abhigyan")
    i+=1

turtle.done()
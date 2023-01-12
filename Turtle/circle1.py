import turtle
win = turtle.Screen()
win.bgcolor("black")
t = turtle.Turtle()
t.color("white")
# ‘fastest’ :  0
# ‘fast’    :  10
# ‘normal’  :  6
# ‘slow’    :  3
# ‘slowest’ :  1
turtle.speed(9)
for i in range(100):
    t.circle(5*i)
    t.circle(-5*i)
    t.left(i)
turtle.exitonclick()
turtle.done()
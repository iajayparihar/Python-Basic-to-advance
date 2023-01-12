import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
wn._color("blue")

sk=turtle.Turtle()

def sqrfunc(size):
    for i in range(4):
        sk.forward(size)
        sk.left(90)
        size -=5

x=145
if x > 0:
    for i in range(7):
        sqrfunc(x)
        x -= 20
        print(x)
turtle.done()
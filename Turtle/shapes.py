import turtle
import time
import random
turtle.speed(0)
print("This program draws shaps based on the number you enter in a uniform pattern .")
num_str = input("Enter the side number of the shape you want to draw :- ")
if num_str.isdigit():
    squares = int(num_str)
angle = 180-180*(squares - 2)/squares
turtle.up()
x,y=0,0
turtle.setpos(x,y)
numshapes=80

for x in range(numshapes):
    turtle.color(random.random(),random.random(),random.random())
    x += 5 
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        turtle.forward(40)
        # print(turtle.pos())
        turtle.up()
        turtle.end_fill()
# time.sleep(5)
# turtle.bye()
turtle.done()

# num_str = input("Enter the side number of the shape you want to draw :- ")
# if num_str.isdigit():
#     squares = int(num_str)
#     print(squares)
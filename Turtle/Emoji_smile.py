from turtle import *
# speed(1)
shape("turtle") # cursor shape change 
pendown()
begin_fill()
color("yellow")
circle(100)
end_fill()

radius=60
mouth_rad=radius * 0.6
mouth_angle=70
penup()
color("black")
setpos(0,mouth_rad)
# setheading(0)
pendown()
circle(mouth_rad,mouth_angle)
penup()
setpos(0,mouth_rad)
setheading(0)
pendown()
circle(mouth_rad,-mouth_angle)
penup()

eye_x =50
eye_y =120
eye_size=60
setpos(eye_x,eye_y)
pendown()
dot(eye_size)
penup()
dot(eye_size)
# home()
setpos(-eye_x,eye_y)
pendown()
dot(eye_size)
penup()
dot(eye_size)

done()
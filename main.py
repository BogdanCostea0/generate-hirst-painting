# paint a 10 by 10 painting with circles with turtle
import turtle as t
import random

t.colormode(255)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

ypos = -250
for i in range(0, 10):
    tim.setx(-200)
    tim.sety(ypos + 50)
    for j in range(0, 10):
        tim.dot(30, random.choice(color_list))
        tim.forward(50)
    ypos += 50
    
screen = t.Screen()
screen.exitonclick()

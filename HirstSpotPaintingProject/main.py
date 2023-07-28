import turtle as turt
from turtle import Screen
from colors import random_color

random_turtle = turt.Turtle()
turt.colormode(255)


def hirst_dot_painting(turtle):
    x, y = 0, 0
    for steps in range(1, 102):
        turtle.hideturtle()
        turtle.penup()
        turtle.dot(20, random_color())
        turtle.setposition(x, y)
        x += 50
        if steps % 10 == 0:
            x = 0
            y += 50
    screen = Screen()
    screen.exitonclick()


hirst_dot_painting(random_turtle)

from turtle import Turtle, Screen, colormode
from random import choice, randint

colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colors = (r, g, b)
    return colors


tim = Turtle()
tim.speed(0)
# for i in range(36):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.right(10)

def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        
draw_spirograph(10)

screen = Screen()
screen.exitonclick()
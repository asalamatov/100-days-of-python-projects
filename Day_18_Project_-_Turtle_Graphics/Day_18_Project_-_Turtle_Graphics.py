from turtle import Turtle, Screen, colormode
from random import *

timmy = Turtle()
colormode(255)

timmy.shape("turtle")

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colors = (r, g, b)
    return colors
    
directions = [0, 90, 180, 270]

s = 3
timmy.pensize(10)
timmy.speed(100)
while s<200:
    timmy.color(random_color())
    timmy.forward(30)
    timmy.right(choice(directions))
    s+=1
    


screen = Screen()
screen.exitonclick()

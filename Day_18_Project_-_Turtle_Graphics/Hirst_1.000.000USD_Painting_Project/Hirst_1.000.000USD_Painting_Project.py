"""
works in PyCharm only
"""

# import colorgram
#
# colors = colorgram.extract('image.jpg', 20)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(251, 249, 245), (208, 165, 125), (250, 235, 237), (140, 49, 106), (164, 169, 38), (244, 80, 57), (230, 114, 163), (3, 143, 55), (215, 234, 232), (241, 65, 140), (1, 143, 184), (162, 55, 52), (50, 203, 226), (254, 230, 0), (21, 166, 126), (245, 224, 47), (212, 235, 238), (28, 196, 219), (119, 184, 146), (231, 167, 191)]

from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)
tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = Screen()
screen.exitonclick()

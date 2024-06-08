# import colorgram
import turtle as t
import random

# Code to extract colors from jpg image file
# rgb_color = []
# extracted_colors = colorgram.extract('spots.jpg', 10)
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     r_g_b = (r, g, b)
#     rgb_color.append(r_g_b)
#
# print(rgb_color)

t.colormode(255)
color_list = [(250, 238, 19), (200, 13, 31), (39, 76, 190), (38, 218, 72), (228, 159, 47), (236, 225, 6), (29, 39, 154)]
s = t.Turtle()
s.hideturtle()
s.speed("fastest")
s.setheading(225)
s.penup()
s.forward(300)
s.setheading(0)
n = 10


def place_dots(n_dots):
    for dot in range(n_dots):
        s.dot(10, random.choice(color_list))
        s.forward(50)


def l_turn():
    s.setheading(90)
    s.forward(50)
    s.setheading(180)
    # s.dot(10, random.choice(color_list))
    s.forward(50)


def r_turn():
    s.setheading(90)
    s.forward(50)
    s.setheading(0)
    s.forward(50)

for i in range(4):
    place_dots(n)
    l_turn()
    place_dots(n)
    r_turn()
    # place_dots(n)

screen = t.Screen()
screen.exitonclick()

# Class and OOPs concepts
# import turtle
import turtle
from turtle import Turtle
import random

# import prettyTables
# import prettytable
#
# table = prettytable.PrettyTable()
# table.add_column("Name", ["Manish", "Dushyant", "Pooja"])
# table.add_column("Type", ["male", "male", "female"])
#
# table.align = 'l'
# print(table)

speedy = Turtle()
print(speedy)
# speedy.shape("turtle")

# speedy.color("green")
speedy.shapesize(1)  # Size of the turtle on screen
speedy.speed("fastest")

# speedy.forward(100)
# speedy.right(90)
# speedy.forward(100)
# speedy.right(90)
# speedy.forward(100)
# speedy.right(90)
# speedy.forward(100)
# speedy.right(90)


# def square_by_turtle(steps):
#     for i in range(4):
#         speedy.forward(steps)
#         speedy.right(90)

# square_by_turtle(250)
# def dash_walk(dash_steps):
#     for step in range(dash_steps):
#         if step % 2 == 0:
#             speedy.penup()
#             speedy.forward(10)
#         else:
#             speedy.pendown()
#             speedy.forward(10)
#
#
# dash_walk(20)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

turtle.colormode(255)
for circles in range(72):
    speedy.color(random_color())
    speedy.circle(100)
    speedy_heading = speedy.heading()
    speedy.setheading(speedy_heading+5)

# speedy.color(random_color())
# speedy.circle(100)

my_screen = turtle.Screen()
my_screen.exitonclick()
print(my_screen)

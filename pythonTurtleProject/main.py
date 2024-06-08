import turtle as t

s = t.Turtle()
s.shape()
screen = t.Screen()  # importing screen for showing turtle platform


def move_ahead():
    """ Function will move turtle 10 steps forward """
    s.forward(10)


def move_back():
    """ Function will move turtle 10 steps backward"""
    s.backward(10)


def move_left():
    """ Function will turn turtle upward by 10 degree anti-clockwise """
    # new_heading = s.heading() + 10
    # s.setheading(new_heading)
    s.left(10)


def move_right():
    """ Function will turn turtle downward by 10 degree clockwise"""
    # new_heading = s.heading() + 10
    # s.setheading(new_heading)
    s.right(10)


def clear_screen():
    s.clear()
    s.penup()
    s.home()
    s.pendown()


screen.listen()
screen.onkey(move_ahead, "d")
screen.onkey(move_back, "a")
screen.onkey(move_right, "s")
screen.onkey(move_left, "w")
screen.onkey(clear_screen, "c")

screen.exitonclick()  # Stop/Hold screen to show results on screen and close it on click

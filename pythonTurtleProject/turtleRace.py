import turtle as t
import random

colors = ["red", "green", "blue", "orange", "purple", "yellow"]
y_axis = [-50, -20, 10, 40, 70, 100]
screen = t.Screen()  # importing screen for showing turtle platform
all_turtles = []
screen.setup(width=500, height=450)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race:\n"
                                                          " 1. Red\n 2. Green\n "
                                                          "3. Blue\n 4. Orange\n "
                                                          "5. Purple\n 6. Yellow")

for n_turtle in range(0, 6):
    s = t.Turtle(shape="turtle")
    s.color(colors[n_turtle])
    s.penup()
    s.goto(x=-240, y=y_axis[n_turtle])
    all_turtles.append(s)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! the {winning_color} turtle won the race")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()  # Stop/Hold screen to show results on screen and close it on click

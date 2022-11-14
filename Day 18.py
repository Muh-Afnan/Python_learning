from turtle import Turtle, Screen
from random import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# terry = Turtle()
# terry.shape("turtle")
# terry.color("red")
# timmy.fillcolor("Black")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
    # terry.forward(100)
    # terry.left(90)

# for _ in range(4):
#     terry.forward(100)
#     terry.left(90)
#
screen = Screen()
screen.exitonclick()
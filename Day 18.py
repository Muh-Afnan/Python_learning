from turtle import Turtle, Screen
from random import random
import heroes

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# terry = Turtle()
# terry.shape("turtle")
# terry.color("red")
# timmy.fillcolor("Black")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
    # terry.forward(100)
    # terry.left(90)

# for _ in range(4):
#     terry.forward(100)
#     terry.left(90)
# timmy.pensize(10)
# for _ in range(4):
#     for _ in range (10):
#         timmy.pendown()
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#     timmy.left(90)
    # timmy.pendown()
    # timmy.forward(10)
    # timmy.penup()
    # timmy.forward(10)

# timmy.left(90)
# for _ in range (10):
#     # timmy.left(90)
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

for _ in range (1):
    for _ in range (3):
        timmy.left(-120)
        timmy.forward(40)
    for _ in range (4):
        timmy.left(-90)
        timmy.forward(40)
    for _ in range (5):
        timmy.left(-75)
        timmy.forward(40)
    # for _ in range (6):
    #     timmy.left(-60)
    #     timmy.forward(40)



screen = Screen()
screen.exitonclick()
#
# print(heroes.gen())

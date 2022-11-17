# import turtle
# from turtle import Turtle, Screen
# import random
# import heroes
#
# timmy = Turtle()
# timmy.shape("classic")
# timmy.color("green")
import turtle
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

# for _ in range (1):
#     for _ in range (3):
#         timmy.pencolor("red")
#         timmy.left(-360/3)
#         timmy.forward(100)
#     for _ in range (4):
#         timmy.pencolor("green")
#         timmy.left(-360/4)
#         timmy.forward(100)
#     for _ in range (5):
#         timmy.pencolor("blue")
#         timmy.left(-360/5)
#         timmy.forward(100)
#     for _ in range (6):
#         timmy.pencolor("yellow")
#         timmy.left(-360/6)
#         timmy.forward(100)
#     for _ in range (7):
#         timmy.pencolor("orange")
#         timmy.left(-360/7)
#         timmy.forward(100)
#     for _ in range (8):
#         timmy.pencolor("black")
#         timmy.left(-360/8)
#         timmy.forward(100)
#     for _ in range (9):
#         timmy.pencolor("blue")
#         timmy.left(-360/9)
#         timmy.forward(100)
#     for _ in range (10):
#         timmy.pencolor("red")
#         timmy.left(-360/10)
#         timmy.forward(100)

# def angle(sides):
#     return 360/sides

# colors = ["aquamarine", "deep sky blue", "lawn green", "midnight blue", "dark olive green", "blue violet"]
# # direction = ["90","180", "-90", "-180", "270", "-270", '360', '-360']
# direction = [0, 90, 180, 270]
# direction = [left, Right]
# def shape(sides):
#     for _ in range(sides):
#         timmy.pencolor(fill)
#         angle = 360 / sides
#         timmy.left(-angle)
#         timmy.forward(100)
# #
# #
# for _ in range(3,11):
#     fill = random.choice(colors)
#     shape(_)


# sides = 2
# for _ in range(7):
#     sides += 1
#     for _ in range(sides):
#         view = -360 / sides
#         timmy.left(view)
#         timmy.forward(100)


# def path():
#     timmy.pensize(10)
#     timmy.speed(10)
#     timmy.pencolor(random.choice(colors))
#     # timmy.left(random.choice(direction))
#     timmy.setheading(random.choice(direction))
#     # timmy. left(side)
#     timmy.forward(40)
#
# for _ in range(100):
#     # side = int(random.choice(direction))
#     # print(type(side))
#     path()
#

# turtle.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,225)
#     b = random.randint(0, 255)
#     my_tupple = (r, g, b)
#     return my_tupple
#
#
# def draw_spirograph(gap):
#     for _ in range(int (360 / gap)):
#         timmy.pencolor(random_color())
#         timmy.speed(0)
#         timmy.circle(100)
#         timmy.heading()
#         current_heading = timmy.heading() + gap
#         timmy.setheading(current_heading)
#
#
# draw_spirograph(5)
#
# screen = Screen()
# screen.exitonclick()

###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

from turtle import Turtle, Screen
from random import choice
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle.colormode(255)
extracted_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
timmy = Turtle()
# turtle.dot(5, "Green")
# turtle.forward(100)
# color = choice(extracted_colors)
# color = choice(extracted_colors)
# print(color)
# for _ in range (10):
#     timmy.penup()
#     timmy.dot(20, choice(extracted_colors))
#     timmy.fd(50)
turtle.colormode(255)
extracted_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed(0)

timmy.showturtle()
var = 0
for _ in range (10):
    var += 1
    for _ in range (10):
        timmy.dot(20, choice(extracted_colors)); timmy.penup(); timmy.fd(50); timmy.dot(20, choice(extracted_colors))
    if var < 10:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()

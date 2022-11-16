# import turtle
# from turtle import Turtle, Screen
# import random
# import heroes
#
# timmy = Turtle()
# timmy.shape("classic")
# timmy.color("green")


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

colors = ["aquamarine", "deep sky blue", "lawn green", "midnight blue", "dark olive green", "blue violet"]
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
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

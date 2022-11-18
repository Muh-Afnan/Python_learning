import random
from turtle import Turtle, Screen

# timmy = Turtle();timmy.shape("turtle");timmy.color("green");timmy.penup()
# jenny = Turtle();jenny.shape("turtle");jenny.color("red");jenny.penup()
# freaky = Turtle();freaky.shape("turtle");freaky.color("black");freaky.penup()
# domy = Turtle();domy.shape("turtle");domy.color("blue");domy.penup()


# timmy = Turtle();timmy.shape("turtle");timmy.color("green");timmy.penup();timmy.goto(x=-240, y=0)
# jenny = Turtle();jenny.shape("turtle");jenny.color("red");jenny.penup();jenny.goto(x=-240, y=75)
# freaky = Turtle();freaky.shape("turtle");freaky.color("black");freaky.penup();freaky.goto(x=-240, y=-75)
# domy = Turtle();domy.shape("turtle");domy.color("blue");domy.penup();domy.goto(x=-240, y=-150)
# gomy = Turtle();gomy.shape("turtle");gomy.color("orange");gomy.penup();gomy.goto(x=-240, y=150)


#
# def move_forward():
#      tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def counter_clockwise():
#     tim.left(10)
#
# def clockwise():
#     tim.right(10)
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="W", fun=move_forward)
# # screen.onkey(move_forward, "W")
# screen.onkey(key="S", fun=move_backward)
# screen.onkey(key="A", fun=counter_clockwise)
# screen.onkey(key="D", fun=clockwise)
# screen.onkey(key="C", fun=clear_drawing)

speed = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "green", "blue", "black", "orange", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
timmies =[]
is_race_on = False

for turtle_index in range (0, 6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(color[turtle_index])
    timmy.goto(x=-230, y=(y_position[turtle_index]))
    timmies.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:

    for timmy in timmies:
        if timmy.xcor() > 230:
            is_race_on = False
            wining_color = timmy.pencolor()
            if wining_color == user_bet:
                print(f"You have won!. The {wining_color} turtle is the winner!")
            else:
                print(f"You have lost!. The {wining_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        timmy.forward(rand_distance)


screen.exitonclick()





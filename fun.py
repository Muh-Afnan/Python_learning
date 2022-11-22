from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()
screen.listen()

def up():
    timmy.setheading(90)


def down():
    timmy.setheading(270)


def left():
    timmy.setheading(180)

def right():
    timmy.setheading(0)


screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")





screen.exitonclick()
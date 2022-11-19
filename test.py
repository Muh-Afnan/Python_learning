from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake")
screen.tracer(0)

location = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in location:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    for seg in segments:
        seg.forward(20)
        segments[0].left(90)
        segments[1].left(90)
        segments[2].left(90)

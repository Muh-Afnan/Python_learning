import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
screen.tracer(0)

location = [0, -20, 20]

snake_health = []

for index in range (0, 3):
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(x= (location[index]), y=0)
    snake_health.append(snake)

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake in snake_health:
        snake.forward(20)

screen.exitonclick()

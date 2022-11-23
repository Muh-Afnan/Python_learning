import time
from turtle import Turtle,Screen
from snake20 import Snake
from Food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# location = [0, -20, 20]
#
# snake_health = []
#
# for index in range (0, 3):
#     snake = Turtle("square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(x= (location[index]), y=0)
#     snake_health.append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for snake_num in range (len(snake_health)-1, 0, -1):
    #     new_x = snake_health[snake_num-1].xcor()
    #     new_y = snake_health[snake_num-1].ycor()
    #     snake_health[snake_num].goto(x=new_x, y=new_y)
    # snake_health[0].forward(20)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.count_score()

screen.exitonclick()

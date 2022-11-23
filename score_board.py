from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update()
    def update(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
    def count_score(self):
        self.score +=1
        self.clear()
        self.update()
    def game_is_over(self):
        self.goto(x=0, y=0)
        self.write("Game is Over", align="center", font=("Arial", 24, "normal"))
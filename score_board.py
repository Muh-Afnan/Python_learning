from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.hideturtle()
        # self.speed("fastest")
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
        # self.goto(x=0, y=280)
    def count_score(self):
        self.sccore +=1
from turtle import Turtle
import random
# score = 0
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        self.score = 0

    def refresh(self):
        self.goto(x=random.randrange(-280 , 280),y=random.randrange(-280 , 280))

    def count_score(self):
        self.score += 1
        print(self.score)

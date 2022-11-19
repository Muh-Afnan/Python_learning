from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __int__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move(self):
        for snake_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)
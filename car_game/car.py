from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class Cars(Turtle):

    def __init__(self, x_move):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.uniform(-280, 280))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.x_move = x_move * random.uniform(0.8,1.2)

    def move(self):
        self.goto(self.xcor() - self.x_move, self.ycor())

    def level_up(self):
        self.x_move = self.x_move + MOVE_INCREMENT

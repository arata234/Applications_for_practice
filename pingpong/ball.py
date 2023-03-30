from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    def bounce(self):
        self.y_move *= -1
    
    def reflect(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1

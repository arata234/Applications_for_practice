from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed('fastest')
        posi_x = random.randint(-260, 260)
        posi_y = random.randint(-260, 260)
        self.goto(posi_x, posi_y)
    
    def refresh(self):
        posi_x = random.randint(-260, 260)
        posi_y = random.randint(-260, 260)
        self.goto(posi_x, posi_y)
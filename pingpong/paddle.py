from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, y_pos)
    
    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)
    
    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
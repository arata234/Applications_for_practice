from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    # def down(self):
    #     self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
    
    def level_up(self):
        self.goto(STARTING_POSITION)

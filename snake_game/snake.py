from turtle import Turtle
import time


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake(object):
    
    def __init__(self):
        self.segments = []
        self.init_snake()
        self.head = self.segments[0]

    def init_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)
    
    def add_snake(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_snake(self.segments[-1].position())
    
    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            move_x = self.segments[seg-1].xcor()
            move_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(move_x, move_y)
        self.head.forward(DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
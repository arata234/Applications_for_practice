from turtle import Turtle
import random

Y_POS = 250

SHAPE = {"T": [(10, Y_POS), (10, Y_POS-20), (-10, Y_POS-20), (30, Y_POS-20)], 
         "Z": [(-10, Y_POS), (10, Y_POS), (10, Y_POS-20), (30, Y_POS-20)], 
         "S": [(30, Y_POS), (10, Y_POS), (10, Y_POS-20), (-10, Y_POS-20)], 
         "O": [(10, Y_POS), (-10, Y_POS), (10, Y_POS-20), (-10, Y_POS-20)], 
         "I": [(-30, Y_POS), (-10, Y_POS), (10, Y_POS), (30, Y_POS)], 
         "L": [(10, Y_POS), (10, Y_POS-20), (-10, Y_POS-20), (-30, Y_POS-20)], 
         "J": [(-10, Y_POS), (-10, Y_POS-20), (10, Y_POS-20), (30, Y_POS-20)]}


class Block(object):
    
    def __init__(self):
        self.blocks = []
        self.state = {"T": 0, "Z": 0, "S": 0, "O": 0, "I": 0, "L": 0, "J": 0}
        self.shape = random.choice(list(SHAPE.keys()))
        self.generate_block(self.shape)
    
    def generate_block(self, shape):
        self.state = {"T": 0, "Z": 0, "S": 0, "O": 0, "I": 0, "L": 0, "J": 0}
        if shape == "T":
            for i in SHAPE[shape]:
                t_block = Turtle("square")
                t_block.color("purple")
                t_block.penup()
                t_block.setheading(270)
                t_block.goto(i)
                self.blocks.append(t_block)
        
        if shape == "Z":
            for i in SHAPE[shape]:
                t_block = Turtle("square")
                t_block.color("red")
                t_block.penup()
                t_block.setheading(270)
                t_block.goto(i)
                self.blocks.append(t_block)
                
        if shape == "S":
            for i in SHAPE[shape]:
                t_block = Turtle("square")
                t_block.color("green")
                t_block.penup()
                t_block.setheading(270)
                t_block.goto(i)
                self.blocks.append(t_block)
                
        if shape == "O":
            for i in SHAPE[shape]:
                t_block = Turtle("square")
                t_block.color("yellow")
                t_block.penup()
                t_block.setheading(270)
                t_block.goto(i)
                self.blocks.append(t_block)
                
        if shape == "I":
            for i in SHAPE[shape]:
                t_block = Turtle("square")
                t_block.color("cyan")
                t_block.penup()
                t_block.setheading(270)
                t_block.goto(i)
                self.blocks.append(t_block)
                
        if shape == "L":
            for i in SHAPE[shape]:
                t_block = Turtle("square")
                t_block.color("blue")
                t_block.penup()
                t_block.setheading(270)
                t_block.goto(i)
                self.blocks.append(t_block)
                
        if shape == "J":
            for i in SHAPE[shape]:
                t_block = Turtle("square")
                t_block.color("orange")
                t_block.penup()
                t_block.setheading(270)
                t_block.goto(i)
                self.blocks.append(t_block)
    
    def fall(self):
        for block in self.blocks:
            block.forward(20)
    
    def left(self):
        if all([block.xcor() > -90  for block in self.blocks]):
            for block in self.blocks:
                block.goto(block.xcor()-20, block.ycor())

    def right(self):
        if all([block.xcor() < 90  for block in self.blocks]):
            for block in self.blocks:
                block.goto(block.xcor()+20, block.ycor())
                
    def rotate(self):
        shape = self.shape
        if shape == "T":
            self.rotate_T()
            
        if shape == "Z":
            self.rotate_Z()
            
        if shape == "S":
            self.rotate_S()
        
        if shape == "I":
            self.rotate_I()
        
        if shape == "L":
            self.rotate_L()
            
        if shape == "J":
            self.rotate_J()
     
    
    def in_wall(self):
        for block in self.blocks:
            if block.xcor() >= 90:
                for block in self.blocks:
                    block.goto(block.xcor()-20, block.ycor())
            elif block.xcor() <= -90:
                for block in self.blocks:
                    block.goto(block.xcor()+20, block.ycor())
            
                
    def rotate_T(self, shape="T"):
        if self.state[shape] == 0:
            self.blocks[2].goto(self.blocks[2].xcor()+20, self.blocks[2].ycor()+40)
            self.blocks[3].goto(self.blocks[3].xcor(), self.blocks[3].ycor()+20)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 1:
            self.blocks[2].goto(self.blocks[2].xcor()-20, self.blocks[2].ycor()-20)
            self.in_wall()
            self.state[shape] += 1
            return
        
        if self.state[shape] == 2:
            self.blocks[3].goto(self.blocks[3].xcor()-20, self.blocks[3].ycor()+20)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 3:
            self.blocks[1].goto(self.blocks[1].xcor()+20, self.blocks[1].ycor()+20)
            self.blocks = [self.blocks[3], self.blocks[0], self.blocks[2], self.blocks[1]]
            self.in_wall()
            self.state[shape] = 0
            return
    
    def rotate_Z(self, shape="Z"):
        if self.state[shape] == 0:
            self.blocks[2].goto(self.blocks[2].xcor()-20, self.blocks[2].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()-20, self.blocks[3].ycor()+40)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 1:
            self.blocks[2].goto(self.blocks[2].xcor()+20, self.blocks[2].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()+20, self.blocks[3].ycor()-40)
            self.in_wall()
            self.state[shape] = 0
            return
        
    def rotate_S(self, shape="S"):
        if self.state[shape] == 0:
            self.blocks[2].goto(self.blocks[2].xcor()+20, self.blocks[2].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()+20, self.blocks[3].ycor()+40)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 1:
            self.blocks[2].goto(self.blocks[2].xcor()-20, self.blocks[2].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()-20, self.blocks[3].ycor()-40)
            self.in_wall()
            self.state[shape] = 0
            return
        
    def rotate_I(self, shape="I"):
        if self.state[shape] == 0:
            self.blocks[0].goto(self.blocks[0].xcor()+40, self.blocks[0].ycor()+40)
            self.blocks[1].goto(self.blocks[1].xcor()+20, self.blocks[1].ycor()+20)
            self.blocks[3].goto(self.blocks[3].xcor()-20, self.blocks[3].ycor()-20)
            self.in_wall()
            self.state[shape] += 1
            return
        
        if self.state[shape] == 1:
            self.blocks[0].goto(self.blocks[0].xcor()-40, self.blocks[0].ycor()-40)
            self.blocks[1].goto(self.blocks[1].xcor()-20, self.blocks[1].ycor()-20)
            self.blocks[3].goto(self.blocks[3].xcor()+20, self.blocks[3].ycor()+20)
            self.in_wall()
            self.state[shape] = 0
            return
    
    def rotate_L(self, shape="L"):
        if self.state[shape] == 0:
            self.blocks[0].goto(self.blocks[0].xcor()-20, self.blocks[0].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()+20, self.blocks[3].ycor()+40)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 1:
            self.blocks[0].goto(self.blocks[0].xcor(), self.blocks[0].ycor()-40)
            self.blocks[3].goto(self.blocks[3].xcor()+40, self.blocks[3].ycor()-40)
            self.in_wall()
            self.state[shape] += 1
            return
        
        if self.state[shape] == 2:
            self.blocks[0].goto(self.blocks[0].xcor()+20, self.blocks[0].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()-20, self.blocks[3].ycor()-40)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 3:
            self.blocks[0].goto(self.blocks[0].xcor(), self.blocks[0].ycor()+40)
            self.blocks[3].goto(self.blocks[3].xcor()-40, self.blocks[3].ycor()+40)
            self.in_wall()
            self.state[shape] = 0
            return
        
    def rotate_J(self, shape="J"):
        if self.state[shape] == 0:
            self.blocks[0].goto(self.blocks[0].xcor(), self.blocks[0].ycor()-40)
            self.blocks[3].goto(self.blocks[3].xcor()-40, self.blocks[3].ycor()-40)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 1:
            self.blocks[0].goto(self.blocks[0].xcor()+20, self.blocks[0].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()-20, self.blocks[3].ycor()+40)
            self.in_wall()
            self.state[shape] += 1
            return
        
        if self.state[shape] == 2:
            self.blocks[0].goto(self.blocks[0].xcor(), self.blocks[0].ycor()+40)
            self.blocks[3].goto(self.blocks[3].xcor()+40, self.blocks[3].ycor()+40)
            self.in_wall()
            self.state[shape] += 1
            return
            
        if self.state[shape] == 3:
            self.blocks[0].goto(self.blocks[0].xcor()-20, self.blocks[0].ycor())
            self.blocks[3].goto(self.blocks[3].xcor()+20, self.blocks[3].ycor()-40)
            self.in_wall()
            self.state[shape] = 0
            return
        
    def remove_block(self):
        self.blocks = []
from turtle import Turtle

WALL_WIDTH = 20
BLOCK_SIZE = 20
LEFT_X = -90

class Wall(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_grid()
        self.walls = []
        for i in range(-210, 210, WALL_WIDTH):
            self.create_wall(-110, i)
            self.create_wall(-110+BLOCK_SIZE*11, i)
        for i in range(-90, -90+BLOCK_SIZE*10, WALL_WIDTH):
            self.create_wall(i, -210)
        
    def create_grid(self):
        grid = Turtle("arrow")
        grid.color("gray")
        for i in range(-200, 220, 20): 
            grid.penup()
            grid.goto(-110, i)
            grid.pendown()
            grid.goto(-110+BLOCK_SIZE*11, i)
        
        for i in range(-100, 120, 20):
            grid.penup()
            grid.goto(i, 200)
            grid.pendown()
            grid.goto(i, -200)
        
        grid.penup()
        grid.goto(10000, 10000)

    
    def create_wall(self, x_pos, y_pos): 
        new_wall = Turtle("square")
        # new_wall.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_wall.color("white")
        new_wall.penup()
        new_wall.goto(x_pos, y_pos)
        self.walls.append(new_wall)
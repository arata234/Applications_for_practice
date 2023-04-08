import wall
import block

from turtle import Screen
from turtle import Turtle
import time
import random

SHAPE = ["T", "Z", "S", "O", "I", "L", "J"]
TIME_SLEEP = 0.25
all_column = [i for i in range(-90, 90, 20)]
all_row = [i for i in range(-190, 210, 20)]

def fast_down():
    global TIME_SLEEP
    TIME_SLEEP = 0

def vanish_row(exist_list):
    vanish_row_dict = {}
    for y in all_row:
        temp = []
        for block in exist_list:
            if y == block.ycor():
                temp.append(block)
        if len(temp) == 10:
            vanish_row_dict[y] = temp
            for block in temp:
                block.goto(10000, 10000)
                exist_list.remove(block)

            for block in exist_list:
                if block.ycor() > y:
                    block.forward(20)

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=400, height=600)
    screen.bgcolor("black")
    screen.title("Tetris")
    screen.tracer(0)
    
    
    wall = wall.Wall()
    block = block.Block()
    
    exist_blocks = []
    
    screen.listen()
    screen.onkey(block.left, "a")
    screen.onkey(block.right, "d")
    screen.onkey(fast_down, "s")
    screen.onkey(block.rotate, "r")
    
    game_is_on = True
    c = 0
    while game_is_on:
        screen.update()
        time.sleep(TIME_SLEEP)
        if c % 2 == 0:
            block.fall()
        # print([b.position() for b in block.blocks])
        # print([b.ycor() for b in block.blocks])
        
        if any([b.ycor() == -190.0 for b in block.blocks]):
            exist_blocks.extend(block.blocks)
            block.remove_block()
            screen.update()
            block.shape = random.choice(SHAPE)
            block.generate_block(block.shape)
            TIME_SLEEP = 0.25
            
        elif any([abs(e.ycor() - b.ycor()) == 20 and abs(e.xcor() - b.xcor()) < 5 for b in block.blocks for e in exist_blocks]):
            exist_blocks.extend(block.blocks)
            block.remove_block()
            screen.update()
            # print(set(i.position() for i in exist_blocks))
            block.shape = random.choice(SHAPE)
            block.generate_block(block.shape)
            TIME_SLEEP = 0.25
        
        if any(i.ycor() >= 230 for i in exist_blocks):
            game_is_on = False

        vanish_row(exist_blocks)
        
        
        c += 1
    screen.exitonclick()
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
    global tm
    tm = 0

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

def beside_block(current_blocks, exist_list):
    position_list = [block.position() for block in exist_list]
    current_blocks_position_list = [block.position() for block in current_blocks]
    if any([abs(c[0] - p[0]) < 5 and abs(c[1] - p[1]) < 5 for c in current_blocks_position_list for p in position_list]):
        return True



if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=400, height=600)
    screen.bgcolor("black")
    screen.title("Tetris")
    screen.tracer(0)
    
    
    wall = wall.Wall()
    block = block.Block()

    exist_blocks = []
    walls = wall.walls

    screen.listen()
    screen.onkey(block.left, "a")
    screen.onkey(block.right, "d")
    screen.onkey(fast_down, "s")
    screen.onkey(block.rotate, "r")
    
    game_is_on = True
    tm = TIME_SLEEP
    c = 0
    trace_pos_list = []
    while game_is_on:
        screen.update()
        time.sleep(tm)
        if c % 2 == 0:
            block.fall()
        # print([b.position() for b in block.blocks])
        # print([b.ycor() for b in block.blocks])
            trace_pos_list.append([b.position() for b in block.blocks]) 
            
        if any([b.ycor() - e.ycor() == 20 and abs(e.xcor() - b.xcor()) < 5 for b in block.blocks for e in exist_blocks]) or\
              any([b.ycor() - e.ycor() == 20 and abs(e.xcor() - b.xcor()) < 5 for b in block.blocks for e in walls]):
            start = time.time()

            while time.time() - start < 1.0:
                screen.update()
                if beside_block(block.blocks, exist_blocks):
                    for i, b in enumerate(block.blocks):
                        b.goto(trace_pos_list[-1][i])  
                trace_pos_list.append([b.position() for b in block.blocks])

            if any([b.ycor() - e.ycor() == 20 and abs(e.xcor() - b.xcor()) < 5 for b in block.blocks for e in walls]):
                exist_blocks.extend(block.blocks)
                trace_pos_list = []
                block.remove_block()
                screen.update()
                # print(set(i.position() for i in exist_blocks))
                block.shape = random.choice(SHAPE)
                block.generate_block(block.shape)
                tm = TIME_SLEEP

            if not any([abs(b.ycor() - e.ycor()) < 5 and abs(e.xcor() - b.xcor()) < 5 for b in block.blocks for e in exist_blocks]):
                if any([b.ycor() - e.ycor() == 20 and abs(e.xcor() - b.xcor()) < 5 for b in block.blocks for e in exist_blocks]):
                    exist_blocks.extend(block.blocks)
                    trace_pos_list = []
                    block.remove_block()
                    screen.update()
                    # print(set(i.position() for i in exist_blocks))
                    block.shape = random.choice(SHAPE)
                    block.generate_block(block.shape)
                    tm = TIME_SLEEP
        

        # if beside_block(block.blocks, exist_blocks):
        #             for i, b in enumerate(block.blocks):
        #                 b.goto(trace_pos_list[-1][i])
        #             trace_pos_list.append([b.position() for b in block.blocks])

        if any(i.ycor() >= 230 for i in exist_blocks):
            game_is_on = False

        vanish_row(exist_blocks)
        
        
        c += 1
    screen.exitonclick()
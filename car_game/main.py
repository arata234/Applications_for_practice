from turtle import Screen
import time
import random

from player import Player
from car import Cars
from scoreboard import Scoreboard


STARTING_MOVE_DISTANCE = 5
cars = []
def generate_cars(x_move):
    cars.append(Cars(x_move))


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Car Game")
    screen.tracer(0)

    player = Player()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.up, "Up")
    # screen.onkey(player.down, "Down")

    game_is_on = True
    start = int(time.time())
    i = 0

    while game_is_on:
        time.sleep(0.1 - 0.01*i)
        screen.update()
        if random.choice([True, False, False, False]):
            generate_cars(STARTING_MOVE_DISTANCE+i*5*random.uniform(0.8,1.2))

        for car in cars:
            car.move()

        if player.ycor() == 290:
            player.level_up()
            for car in cars:
                car.hideturtle()
            cars = []
            scoreboard.add_score()
            i += 1
        
        if any([player.distance(car) < 25 for car in cars]):
            game_is_on = False
            scoreboard.gameover()


    
    screen.exitonclick()
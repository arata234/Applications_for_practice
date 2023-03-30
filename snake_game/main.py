from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

EAT_DISTANCE = 15



if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)
    
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")
    
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < EAT_DISTANCE:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()
            print("nom nom nom")
            
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()
            
        for segment in snake.segments:
            if segment == snake.head:
                pass
            
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                
        
    screen.exitonclick()
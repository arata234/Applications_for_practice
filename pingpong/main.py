import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("PingPong")
    screen.tracer(0)
    
    paddle_left = Paddle(-360, 0)
    paddle_right = Paddle(350, 0)
    ball = Ball()
    sb = Scoreboard()
    
    screen.listen()
    screen.onkey(paddle_left.go_up, "w")
    screen.onkey(paddle_right.go_up, "Up")
    screen.onkey(paddle_left.go_down, "s")
    screen.onkey(paddle_right.go_down, "Down")
    
    game_is_on = True
    right_reflect = True
    left_reflect = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball.move()
        
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()
        
        if paddle_left.distance(ball) < 40 and paddle_left.xcor() < -350:
            if left_reflect:
                ball.reflect()
            left_reflect = False
            right_reflect = True
        
        if paddle_right.distance(ball) < 40 and paddle_right.xcor() > 340:
            if right_reflect:
                ball.reflect()
            right_reflect = False
            left_reflect = True
        
        if ball.xcor() > 380:
            sb.left_point()
            ball.reset_position()
            
        if ball.xcor() < -380:
            sb.right_point()
            ball.reset_position()
            
            
    screen.exitonclick()
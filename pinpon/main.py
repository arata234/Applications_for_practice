import time
from turtle import Turtle, Screen
from paddle import Paddle

if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("PingPong")
    
    paddle_left = Paddle(-360, 0)
    paddle_right = Paddle(350, 0)
    
    screen.listen()
    screen.onkey(paddle_left.go_up, "w")
    screen.onkey(paddle_right.go_up, "Up")
    screen.onkey(paddle_left.go_down, "s")
    screen.onkey(paddle_right.go_down, "Down")
    
    
    
    
    
    
    
    screen.exitonclick()
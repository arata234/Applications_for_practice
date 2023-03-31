from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"Score: {self.score}", align="center", font=("Coutier", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.update_score()
    
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Coutier", 24, "normal"))
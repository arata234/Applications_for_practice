from turtle import Turtle
import json

with open("./snake_game/high_score.json") as f:
    d = json.load(f)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = d["high_score"]
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()
        self.score = 0
        with open("./snake_game/high_score.json", "w") as f:
            json.dump({"high_score": self.high_score}, f)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
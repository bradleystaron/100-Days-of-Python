# Scoreboard for left and right player in Pong game
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):   
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        
    # Function to update the scoreboard display    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 260)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)
        
    # Function to increase the score depending on which side the ball went out
    def increase_score(self, scorer="right"):
        if scorer == "right":
            self.right_score += 1
        else:
            self.left_score += 1
        self.update_scoreboard()
        
    # Function to reset scores to zero
    def reset(self):
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        
    

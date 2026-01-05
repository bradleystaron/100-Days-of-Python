# Scoreboard File that contains the scoreboard class

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Scoreboard Class that manages the score display
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("100_Days_of_Code_Python/Days_22-25/Projects/Day24/data.txt") as file:
            contents = file.read().strip()

            if contents.isdigit():
                self.high_score = int(contents)
            else:
                self.high_score = 0
        self.score = 0
        # Read high score from file
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    
    #reset the score when the game is over and write high score to file if needed
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("100_Days_of_Code_Python/Days_22-25/Projects/Day24/data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard() 
    
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
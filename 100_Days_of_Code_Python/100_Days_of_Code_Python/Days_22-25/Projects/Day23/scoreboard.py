# Scoreboard class to manage and display the player's score in the crossing the road game
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    # Initialize the scoreboard with level 1
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()   # <-- hides the arrow
        self.penup()        # <-- don't draw lines
        self.goto(-280, 260)
        self.display_scoreboard()
        
    # Display the current level on the screen
    def display_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increase the level by 1 and update the display
    def increase_level(self):
        self.level += 1
        self.display_scoreboard()
        
    # update the scoreboard display
    def update_scoreboard(self):
        self.clear()
        self.display_scoreboard()
    
    # Display game over message
    def display_game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
            
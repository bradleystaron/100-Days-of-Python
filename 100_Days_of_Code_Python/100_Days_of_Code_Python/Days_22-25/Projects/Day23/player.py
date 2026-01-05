# Player class to manage the player's turtle for the crossing the road game
import random
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # movement for the player turtle
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    # move the player turtle up    
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # move the player turtle down
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
      
    # Reset the player to the starting position
    def reset_position(self):
        self.goto(STARTING_POSITION)

    # Check if the player has reached the finish line
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
    
    
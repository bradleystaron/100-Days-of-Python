# Ball file for the Pong game
from turtle import Turtle

BALL_MOVE_DISTANCE = 0.05

# Ball class to manage ball behavior
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = BALL_MOVE_DISTANCE

    # Move the ball in the current direction
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounce the ball off the top and bottom walls
    def bounce_y(self):
        self.y_move *= -1

    # Bounce the ball off the paddles
    def bounce_x(self):
        self.x_move *= -1

    # Reset ball position to center and reverse direction
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
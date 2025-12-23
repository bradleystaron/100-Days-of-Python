from turtle import Turtle, Screen
from paddles import Paddle
from scoreboard import Scoreboard
from ball import Ball

# Set up the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles, ball, and scoreboard objects
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()

# Keyboard bindings
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True

# Main game loop
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.xcor() > 320 and ball.xcor() < 340) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.bounce_x()

    # Detect collision with left paddle
    if (ball.xcor() < -320 and ball.xcor() > -340) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.bounce_x()

    # Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score += 1
        scoreboard.update_scoreboard()

    # Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score += 1
        scoreboard.update_scoreboard()
        
    # Check for winning condition
    if scoreboard.left_score >= 10:
        scoreboard.goto(0, 0)
        scoreboard.write("Left Player Wins!", align="center", font=("Courier", 36, "normal"))
        game_is_on = False
    elif scoreboard.right_score >= 10:
        scoreboard.goto(0, 0)
        scoreboard.write("Right Player Wins!", align="center", font=("Courier", 36, "normal"))
        game_is_on = False
        
        
screen.exitonclick()
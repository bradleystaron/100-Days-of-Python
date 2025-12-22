#Snake Game Program 

from turtle import Turtle, Screen
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#turtle objects for snake head and body
starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
    
#functions to move the snake
def move_up():
    if segments[0].direction != "down":
        segments[0].direction = "up"
        
def move_down():
    if segments[0].direction != "up":
        segments[0].direction = "down"
        
def move_left():
    if segments[0].direction != "right":
        segments[0].direction = "left"
        
def move_right():
    if segments[0].direction != "left":
        segments[0].direction = "right"        


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
        
    if segments[0].direction == "up":
        segments[0].sety(segments[0].ycor() + 20)   
    
    if segments[0].direction == "down":
        segments[0].sety(segments[0].ycor() - 20)
    
    if segments[0].direction == "left":
        segments[0].setx(segments[0].xcor() - 20)
    
    if segments[0].direction == "right":
        segments[0].setx(segments[0].xcor() + 20)
        
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
                    

screen.exitonclick()
import turtle as t
import random

# Etch a sketch program using turtle module
tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
    
def turn_counter_clockwise():
    tim.left(45)

def turn_clockwise():
    tim.right(45)
    
# w key to move the turtle forward
# s key to move the turtle backward
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)


screen.listen()
screen.exitonclick()
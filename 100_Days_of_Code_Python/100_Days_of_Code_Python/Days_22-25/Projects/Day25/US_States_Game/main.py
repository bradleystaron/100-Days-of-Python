# Project Title: US States Game
# Description: A game to guess the names of US states using the turtle graphics library.
import turtle
import pandas as pd
from turtle import Screen

screen = Screen()
screen.title("U.S. States Game")

image = "100_Days_of_Code_Python/Days_22-25/Projects/Day25/US_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("100_Days_of_Code_Python/Days_22-25/Projects/Day25/US_States_Game/50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("100_Days_of_Code_Python/Days_22-25/Projects/Day25/US_States_Game/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        

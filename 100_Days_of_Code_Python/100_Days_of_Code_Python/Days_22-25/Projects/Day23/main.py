# Main file to run the crossing the road game using turtle graphics

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.display_game_over()
            game_is_on = False
            
    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()
        
    # display the scoreboard
    scoreboard.display_scoreboard()
    
    
screen.exitonclick()
 

# CarManager class to manage the cars in the crossing the road game
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Class for managing the random cars in the car crossing game
class CarManager(Turtle):
    
    # Initialize the car manager with an empty list of cars and starting speed
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Move all cars to the left by the current car speed
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    # Create a new car at random intervals        
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # Increase the speed of the cars
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    
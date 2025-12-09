import another_module
from turtle import *

print(another_module.another_variable)  

# new object named timmy
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
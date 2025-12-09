# import another_module
# from turtle import *

# print(another_module.another_variable)  

# # new object named timmy
# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

# This Creates a new PrettyTable object
table = PrettyTable()

# This taps into an objects method to add columns to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# This taps into an objects attribute to change the alignment of the table
table.align = "l"

print(table)
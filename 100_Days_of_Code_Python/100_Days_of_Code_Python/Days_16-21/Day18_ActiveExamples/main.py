# This is an alias import which allows us to use 't' instead of 'turtle' for brevity.
import turtle as t
import random

tim = t.Turtle()

tim.shape("turtle")

# Draws a square
    # tim.shape("turtle")
    # tim.color("LightSkyBlue")
    # tim.forward(100)
    # tim.left(90)
    # tim.forward(100)
    # tim.color("coral")
    # tim.left(90)
    # tim.forward(100)
    # tim.left(90)
    # tim.forward(100)

# Draws a Pentagon
    # for _ in range(5):
    #     tim.forward(100)
    #     tim.left(72)

# Draws shapes with different number of sides and random colors
    # def draw_shape(num_sides):
    #     angle = 360 / num_sides
    #     for _ in range(num_sides):
    #         tim.forward(100)
    #         tim.left(angle)

    # for shape_side_n in range(3, 11):
    #     tim.color(random.choice(colors))
    #     draw_shape(shape_side_n)
    
# Draws a dashed line
    # for _ in range(15):
    #     tim.forward(10)
    #     tim.color("white")
    #     tim.forward(10)
    #     tim.color("black")

# colors = ["DarkOrchid", "DeepPink", "Gold", "LimeGreen", "Turquoise", "DodgerBlue", "Tomato"]

# Walks randomly around the screen in 0, 90, 180, 270 degree angles using pen color at random

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# directions = [0, 90, 180, 270]
tim.pensize(2)
tim.speed("fastest")
# for _ in range(1000):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(20)

# Spirograph drawing
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        
draw_spirograph(10)
        
screen = t.Screen()
screen.exitonclick()
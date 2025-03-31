import turtle as t
import random

tim = t.Turtle()
t.speed(0)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepskyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

angles = [90, 180, 270, 360]

tim.pensize(10)

for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(angles))

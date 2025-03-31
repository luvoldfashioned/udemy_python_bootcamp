# import another_module

# print(another_module.another_variable)

# import turtle

# timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

# attribute에 접근
# car(object).speed(attribute)
my_screen = Screen()
print(my_screen.canvheight)

# method에 접근
# car.stop
my_screen.exitonclick()

import prettytable


from turtle import Turtle, Screen

turtle_object = Turtle()
for i in range(4):
    turtle_object.forward(100)
    turtle_object.right(90)

screen = Screen()
screen.exitonclick()

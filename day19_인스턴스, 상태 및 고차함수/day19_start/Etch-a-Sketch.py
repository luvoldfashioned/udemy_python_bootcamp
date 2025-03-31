# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear Drawing
from turtle import Turtle, Screen


tim = Turtle()
tim.speed("fastest")
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup
    tim.home()
    tim.pendown()


screen.listen()
# 직접 생성하지 않은 메소드를 사용할 때에는 position argument보다 keyword argument를 사용하는게 좋음
screen.onkey(key="w", fun=move_forwards)  # 함수의 인수로 함수를 전달할 때에는 () 붙이지 않음
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

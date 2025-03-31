from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
# 직접 생성하지 않은 메소드를 사용할 때에는 position argument보다 keyword argument를 사용하는게 좋음
screen.onkey(key="space", fun=move_forwards)  # 함수의 인수로 함수를 전달할 때에는 () 붙이지 않음
screen.exitonclick()

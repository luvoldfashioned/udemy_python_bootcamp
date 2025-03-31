from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()
        self.move_distance = STARTING_MOVE_DISTANCE * -1

    def create_cars(self):
        self.rand_x = random.randint(300, 1000)
        self.rand_y = random.randint(-230, 230)
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(self.rand_x, self.rand_y)

    def move(self):
        self.move_distance
        self.forward(self.move_distance)

    def car_level_up(self):
        self.clear()
        self.move_distance -= MOVE_INCREMENT

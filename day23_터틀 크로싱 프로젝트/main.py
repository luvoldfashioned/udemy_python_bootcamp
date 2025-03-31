import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
all_cars = []

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

# make car instances
for car_index in range(0, 40):
    new_car = CarManager()
    all_cars.append(new_car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if all_cars[-1].xcor() < 0:
        for car_index in range(0, 40):
            new_car = CarManager()
            all_cars.append(new_car)

    for car in all_cars:
        car.move()
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.level_up()
        player.player_level_up()
        for car in all_cars:
            car.car_level_up()

screen.exitonclick()

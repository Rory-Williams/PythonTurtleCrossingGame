import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# main running script for car dodging game


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

user = Player()
screen.listen()
screen.onkey(user.move_up, 'Up')

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
spawn_car = 0
spawn_rate = 6
for _ in range(200):
    spawn_car += 1
    if spawn_car == spawn_rate:
        car_manager.create_car()
        spawn_car = 0
    car_manager.move()

while game_is_on:
    spawn_car += 1
    time.sleep(0.1)
    screen.update()
    if spawn_car == 6:
        # create cars every 6th game loop
        car_manager.create_car()
        spawn_car = 0
    car_manager.move()

    for car in car_manager.cars:
        # check for any collisions with turtle
        if abs(user.ycor() - car.ycor()) < 30:
            if user.xcor() >= car.xcor()-20 and user.xcor() <= car.xcor()+20:
                print('collision')
                scoreboard.game_over()
                game_is_on = False

    if user.ycor() > 200:
        # reset game for next level when turtle reaches top of screen
        print('Level complete')
        user.reset()
        car_manager.inc_speed()
        scoreboard.inc_level()
        if spawn_rate > 2:
            spawn_rate -= 1

    car_manager.delete_car()

screen.exitonclick()
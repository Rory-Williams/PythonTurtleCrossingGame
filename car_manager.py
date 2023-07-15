from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_dist = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.pu()
        car.setheading(180)
        car.turtlesize(1, 2)
        car.color(randint(1, 255), randint(1, 255), randint(1, 255))
        car.setpos(300,randint(-200, 180))
        car.for_speed = self.move_dist
        car.for_speed *= randint(70, 130)/100
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(car.for_speed)

    def inc_speed(self):
        self.move_dist += MOVE_INCREMENT

    def delete_car(self):
        for i, car in enumerate(self.cars):
            if car.pos()[0] < -320:
                self.cars.pop(i)
                # print('removed car')

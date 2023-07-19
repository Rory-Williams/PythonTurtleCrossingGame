from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    # create player turtle
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.pu()
        self.setheading(90)
        self.reset()
        # self.turtlesize(20)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)



from turtle import Turtle
FONT = ("Courier", 24, "normal")
COLOUR = 'black'
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 260)
        self.color(COLOUR)
        self.level = 1
        self.write(f'Level: {self.level}', align=ALIGN, font=FONT)

    def inc_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        FONT = ("Courier", 32, "normal")
        self.write(f'GAME OVER', align=ALIGN, font=FONT)


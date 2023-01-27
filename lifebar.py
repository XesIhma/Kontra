from turtle import Turtle

class LifeBar(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("yellow")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(position)

    def show(self, hp):
        lenghtPercent = hp/100
        lenght = int(lenghtPercent*10)
        if lenght < 1:
            lenght = 1
        self.shapesize(stretch_len=lenght)


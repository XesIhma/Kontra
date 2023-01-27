from turtle import Turtle

class Bullet(Turtle):

    def __init__(self, position, speed):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.5)
        self.penup()
        self.x_move = speed
        self.goto(position)
        self.fired = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def fire(self):
        self.fired = 1

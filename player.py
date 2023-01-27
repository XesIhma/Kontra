from turtle import Turtle
from lifebar import LifeBar

def jumpDistance(x):
    lastX = x-1
    lastY = -4.8*lastX*lastX + 48*lastX
    y = -4.8*x*x + 48*x
    jumpDistance = y - lastY

    return jumpDistance

class Player(Turtle):

    def __init__(self, position, hp, sizeX, sizeY, lifeBarPosition):
        super().__init__()
        self.penup()
        self.goto(position)
        self.hp = hp
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.lifeBar = LifeBar(lifeBarPosition)
        self.bullet = None
        self.jumpIteration = 1
        self.isJumping = 0
        self.isFalling = 0
        self.isgoingLeft = 0
        self.isgoingRight = 0

    def goLeft(self):
        self.isgoingLeft = 1
        self.isgoingRight = 0

    def goRight(self):
        self.isgoingLeft = 0
        self.isgoingRight = 1

    def stop(self):
        self.isgoingLeft = 0
        self.isgoingRight = 0

    
    def goingLeft(self, floors):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        if not self.isOnFloor(floors) and not self.isFalling and not self.isJumping:
            self.fall()
    
    def goingRight(self, floors):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        if not self.isOnFloor(floors) and not self.isFalling and not self.isJumping:
            self.fall()
    
    def jump(self):
        self.isJumping = 1

    def jumping(self):
        if self.jumpIteration < 6:
            self.goto(self.xcor(), self.ycor()+jumpDistance(self.jumpIteration))
            self.jumpIteration+=1
        else:
            self.isJumping = 0
            self.isFalling = 1
    
    def fall(self):
        self.isFalling = 1
        self.jumpIteration = 6
        self.goto(self.xcor(),  self.ycor()-1)

    def falling(self, floors):
        self.goto(self.xcor(),  self.ycor()-1)
        for floor in floors:
            distanceFromFloor = self.ycor() - floor['y']
            if self.xcor() > floor['x1'] and self.xcor() < floor['x2'] and distanceFromFloor < abs(jumpDistance(self.jumpIteration)) and self.ycor() >= floor['y']:
                self.isFalling = 0
                self.jumpIteration = 1
                self.goto(self.xcor(), floor['y'])
                return
            
        self.goto(self.xcor(),  self.ycor()+jumpDistance(self.jumpIteration))
        self.jumpIteration+=1


    def isHit(self, bullet):
        if bullet.xcor() > self.xcor()-self.sizeX and bullet.xcor() < self.xcor()+self.sizeX:
            if bullet.ycor() > self.ycor()-self.sizeY and bullet.ycor() < self.ycor()+self.sizeY:
                return 1
        return 0
    def isOnFloor(self, floors):
        result = 0
        for floor in floors:
            distanceFromFloor = self.ycor() - floor['y']
            if self.xcor() > floor['x1'] and self.xcor() < floor['x2'] and self.ycor() >= floor['y'] and self.ycor() < floor['y'] + 30:
                result = 1
        
        return result
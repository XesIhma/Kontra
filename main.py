from turtle import Screen, Turtle
from player import Player
from bullet import Bullet
from lifebar import LifeBar
from scoreboard import Scoreboard
import time

screen = Screen()
screen.register_shape("background.gif")
screen.bgpic("background.gif")
screen.setup(width=1024, height=692)
screen.title("Kontra")

screen.register_shape("player1.gif")
screen.register_shape("player2.gif")
screen.tracer(0)

player1 = Player((-350, 70), 100, 60, 60, (-400, 300))
player1.shape("player1.gif")

player2 = Player((350, 70), 80, 48, 60, (390, 300))
player2.shape("player2.gif")

player1.bullet = Bullet((player1.xcor(), player1.ycor()+35), 30)
player2.bullet = Bullet((player2.xcor(), player2.ycor()+40), -30)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player1.goLeft, "a")
screen.onkeyrelease(player1.stop, "a")
screen.onkeypress(player1.goRight, "d")
screen.onkeyrelease(player1.stop, "d")
screen.onkey(player1.jump, "w")
screen.onkey(player1.fall, "s")
screen.onkey(player1.bullet.fire, "q")

screen.onkeypress(player2.goLeft, "Left")
screen.onkeyrelease(player2.stop, "Left")
screen.onkeypress(player2.goRight, "Right")
screen.onkeyrelease(player2.stop, "Right")
screen.onkey(player2.jump, "Up")
screen.onkey(player2.fall, "Down")
screen.onkey(player2.bullet.fire, "space")
    
floors = [
    {'y' : 70, 'x1' : -512, 'x2' : 512},
    {'y' : -27, 'x1' : -59, 'x2' : 246},
    {'y' : -127, 'x1' : -300, 'x2' : -139},
    {'y' : -226, 'x1' : -512, 'x2' : -260}
]



game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()

    players = [player1, player2]
    for player in players:
        player.lifeBar.show(player.hp)
        player.lifeBar.show(player.hp)

        if player.isJumping:
            player.jumping()
        if player.isFalling:
            player.falling(floors)
        if player.isgoingLeft:
            player.goingLeft(floors)
        if player.isgoingRight:
            player.goingRight(floors)

        if player.bullet.fired:
            player.bullet.move()
        else: 
            player.bullet.goto((player.xcor(), player.ycor()+35))
            
        if player.bullet.xcor() > 512 or player.bullet.xcor() < -512: 
            player.bullet.fired = 0


    if player2.isHit(player1.bullet):
        player1.bullet.fired = 0
        player2.hp -= 20
    
    if player1.isHit(player2.bullet):
        player2.bullet.fired = 0
        player1.hp -= 20

    
    
    if player1.hp <= 0 or player1.ycor() < -346:
        scoreboard.r_point()
        player1.hp = 100
        player1.goto(-350, 71)
        player1.isFalling = 0

    if player2.hp <= 0 or player2.ycor() < -346:
        scoreboard.l_point()
        player2.hp = 100
        player2.goto(350, 71)
        player1.isFalling = 0

    


screen.exitonclick()
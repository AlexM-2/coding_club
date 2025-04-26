import pgzrun
import _random

WIDTH = 400
HEIGHT = 400


def draw():
    screen.fill((30, 0, 50))
    alien.draw()
    gem.draw()
    

gem = Actor("blue_gem.png")
gem.pos = 350, 0

alien = Actor("alien.png")
alien.pos = 30, 50

def update():

    gem.y+= 4
    if gem.y > HEIGHT+15:
        gem.y = -15
    
    if keyboard.left:
        alien.x-= 5
    if keyboard.right:
        alien.x+= 5

pgzrun.go()
import pgzrun

WIDTH = 400
HEIGHT = 400


def draw():
    screen.clear()

    alien.draw()
    gem.draw()
    

gem = Actor("blue_gem.png")
gem.pos = 370, 415

alien = Actor("alien.png")
alien.pos = 30, 50

def update():
    alien.x+= 1
    if alien.x > WIDTH+30:
        alien.x = -30

    gem.y+= 1
    if gem.y > HEIGHT+15:
        gem.y = -15

pgzrun.go()
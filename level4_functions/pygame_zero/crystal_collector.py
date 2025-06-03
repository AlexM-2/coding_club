import pgzrun
import random

WIDTH: int = 400
HEIGHT: int = 400


def draw():

    global game_over, points, lives


    if game_over:

        screen.fill((0, 0, 0))

        screen.draw.text("Game Over!", (50, 150), color= (255,0,0), fontsize= 70)
        screen.draw.text(f"Final Score: {points}", (10, 10), color= (255, 0, 0), fontsize= 30)
    else:

        screen.fill((30, 0, 50))

        gem1.draw()
        gem2.draw()
        gem3.draw()
        gem4.draw()

        player.draw()

        screen.draw.text(f"Score: {points}", (10, 10), color= (255, 255, 255), fontsize= 30)
        screen.draw.text(f"Lives: {lives}", (10, 40), color= (255, 255, 255), fontsize= 30)
        
    

gem1: Actor = Actor("blue_gem.png")
gem1.pos = random.randint(0, 380), 0
gem2: Actor = Actor("green_gem.png")
gem2.pos = random.randint(0, 380), 0
gem3: Actor = Actor("yellow_gem.png")
gem3.pos = random.randint(0, 380), 0
gem4: Actor = Actor("red_gem.png")
gem4.pos = random.randint(0, 380), 0

player: Actor = Actor("alien.png")
player.pos = 30, 300

points: int = 0
lives: int = 10
game_over: bool = False

def reset_gem1():
    gem1.y = -15
    gem1.x = random.randint(0, 380)
def reset_gem2():
    gem2.y = -15
    gem2.x = random.randint(0, 380)
def reset_gem3():
    gem3.y = -15
    gem3.x = random.randint(0, 380)
def reset_gem4():
    gem4.y = -15
    gem4.x = random.randint(0, 380)

def update():

    global game_over

    if game_over:
        return

    global points, lives

    gem1.y+= 2
    gem2.y+= 4
    gem3.y+= 6
    gem4.y+= 8

    if gem1.y > HEIGHT+15:
        reset_gem1()
        lives-= 4
    if gem2.y > HEIGHT+15:
        reset_gem2()
        lives -= 3
    if gem3.y > HEIGHT+15:
        reset_gem3()
        lives-= 2
    if gem4.y > HEIGHT+15:
        lives -= 1
        reset_gem4()
    
    if keyboard.left:
        player.x-= 5
    if keyboard.right:
        player.x+= 5
    if keyboard.up:
        player.y-= 5
    if keyboard.down:
        player.y+= 5
    
    if gem1.colliderect(player):
        points+= 1
        reset_gem1()
    if gem2.colliderect(player):
        points+= 2
        reset_gem2()
    if gem3.colliderect(player):
        points+= 3
        reset_gem3()
    if gem4.colliderect(player):
        points+= 4
        reset_gem4()
    
    if lives < 1:
        game_over = True

pgzrun.go()
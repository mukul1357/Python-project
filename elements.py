import pygame
import os

# display of game window
screen = pygame.display.set_mode((1200, 500))

# PLAYER'S Movement
# assigning images of hero to the arrays right and left
right = [None]*10
for picIndex in range(1, 10):
    right[picIndex - 1] = pygame.image.load(os.path.join("hero", "R" + str(picIndex) + ".png"))
    picIndex += 1

left = [None] * 10
for picIndex in range(1, 10):
    left[picIndex - 1] = pygame.image.load(os.path.join("hero", "L" + str(picIndex) + ".png"))
    picIndex += 1

#   initializing a global variable stepIndex which is used in player function to smoothen the change in images so that main players walking becomes smooth
stepIndex = 0

def player(move_left, move_right, playerX, playerY):
    #   displaying appropriate images of player
    global stepIndex
    if stepIndex >= 36:
        stepIndex = 0
    if move_left:
        # left moving images of player is displayed
        screen.blit(left[stepIndex // 4], (playerX, playerY))
        stepIndex += 1
    elif move_right:
        # right moving images of player is displayed
        screen.blit(right[stepIndex // 4], (playerX, playerY))
        stepIndex += 1
    else:
        # standing images of player is displayed
        playerImg = pygame.image.load(os.path.join("hero", "standing.png"))
        screen.blit(playerImg, (playerX, playerY))



# ENEMY DISPLAY
def enemy(x, y):
    enemyImg = pygame.image.load('enemy.png')
    screen.blit(enemyImg, (x, y))

# OBSTACLE DISPLAY
def obstacle(x, y, z):
    obstacleImg = pygame.image.load('obstacle'+str(z) +'.png')
    screen.blit(obstacleImg, (x, y))

# ENEMY ENERGYBALL DISPLAY
def shoot_energyball(bX, bY):
    energyball = pygame.image.load('energy_blast.png')
    screen.blit(energyball, (bX, bY))

# HERO'S BULLET DISPLAY
def Bullet_fire(x, y):
    bullet = pygame.image.load('bullet.png')
    screen.blit(bullet, (x, y + 115))

# DISPLAYING BACKGROUNDS
def background_display(bg, i, width):
    screen.blit(bg, (i, 0))
    screen.blit(bg, ((width + i), 0))

# DISPLAYING DR. BORA
def bora(playerX, playerY, i, width):
    dr_bora = pygame.image.load('enemymain.png')
    if playerX <= i + width:
        screen.blit(dr_bora, (i + width + 100, 275))
    else:
        screen.blit(dr_bora, (i + width + 100, playerY))
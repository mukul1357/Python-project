import pygame
import os
import random
import sys
from pygame import mixer

# initialize game
pygame.init()
highscore = 0

# window and background
screen = pygame.display.set_mode((1200, 500))
win = 0
win_sound_played_once = 0
kills = 0
life = 1
health = 100
location = 1

# for showing the winning
score = 0
# for showing the original game
#score = 0

bg_img1 = pygame.image.load('location1.png')
bg1 = pygame.transform.scale(bg_img1, (1200, 500))
bg_img2 = pygame.image.load('location2.png')
bg2 = pygame.transform.scale(bg_img2, (1200, 500))
bg_img3 = pygame.image.load('location3.png')
bg3 = pygame.transform.scale(bg_img3, (1200, 500))
bg_img4 = pygame.image.load('location4.png')
bg4 = pygame.transform.scale(bg_img4, (1200, 500))

# fonts and colors
font = pygame.font.SysFont('forte', 50)
fontbig = pygame.font.SysFont('georgia', 120)
menufont = pygame.font.SysFont('None', 80)
menufontsmall = pygame.font.SysFont('None', 40)
menufontsupersmall = pygame.font.SysFont('None', 25)
menufontbig = pygame.font.SysFont('None', 160)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)

width = 1200
i = 0
# Window and Background
pygame.display.set_caption("ROBOT WAR")
icon = pygame.image.load('gameicon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load(os.path.join("hero", "standing.png"))
playerX = 50
playerY = 275
vel_Y = 20

# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(1200, 2400)
enemyY = random.randint(100, 340)

# obstacle
obstacleImg1 = pygame.image.load('obstacle1.png')
obstacleImg2 = pygame.image.load('obstacle2.png')
obstacleImg3 = pygame.image.load('obstacle3.png')
obstacleImg4 = pygame.image.load('obstacle4.png')
obstacleImg = [obstacleImg1, obstacleImg2, obstacleImg3, obstacleImg4]
obstacleX = random.randint(1200, 3000)
obstacleY = 305

# Bullet
bulletX = 80
bulletY = playerY
vel_bul = 30

# energy ball
ballX = random.randint(1200, 7200)
ballY = random.randint(160, 400)
vel_ball = 25

# Player icons
right = [None] * 10
for picIndex in range(1, 10):
    right[picIndex - 1] = pygame.image.load(os.path.join("hero", "R" + str(picIndex) + ".png"))
    picIndex += 1

left = [None] * 10
for picIndex in range(1, 10):
    left[picIndex - 1] = pygame.image.load(os.path.join("hero", "L" + str(picIndex) + ".png"))
    picIndex += 1

stepIndex = 0

# Controls
move_left = False
move_right = False
jump = False
shoot = False
sprint = False

def startmenu():
    k = 0
    while 1:
        # additional window
        controls_screen = pygame.image.load('controls_screen.png')
        # main background of startscreen and its display
        startscreen = pygame.image.load('warrobot.png')
        screen.blit(startscreen, (0, 0))

        # contents to be displayed
        Title = menufontbig.render('ROBOT WARS', True, RED)

        I = [None] * 12
        I[0] = menufontsupersmall.render('> Complete all the 4 locations and catch Dr. Bora who is hiding ', True, WHITE)
        I[1] = menufontsupersmall.render('   with the help of his invisibilty serum and trying to misuse ', True, WHITE)
        I[2] = menufontsupersmall.render('   Dr. Vaseekaran\'s robots. ', True, WHITE)
        I[3] = menufontsupersmall.render('> Contact with Robots or Obstacles instantly kills the Player ', True, WHITE)
        I[4] = menufontsupersmall.render('   and contact with the bullets will reduce the Players\' Health.', True, WHITE)
        I[5] = menufontsupersmall.render('> If the Health becomes 0 % then the Player dies.', True, WHITE)
        I[6] = menufontsupersmall.render('> Score, Health and number of kills along and the location can be ', True, WHITE)
        I[7] = menufontsupersmall.render('   viewed on the screen.', True, WHITE)
        I[8] = menufontsupersmall.render('> Score could be increased by both continuing forward in the', True, WHITE)
        I[9] = menufontsupersmall.render('   game and killing the enemy robots. movingbcakwards in the', True, WHITE)
        I[10] = menufontsupersmall.render('   game decreses the Score. ', True, WHITE)
        I[11] = menufontsupersmall.render('> location change depends upon the Score.', True, WHITE)

        horizontalmovement = menufontsmall.render('> Arrow keys for sideways movement', True, WHITE)
        verticalmovement = menufontsmall.render('> \'J\' (or) UP arrow key to jump', True, WHITE)

        bulletON = menufontsmall.render('> \'B\' to shoot a bullet', True, WHITE)

        runmovementON = menufontsmall.render('> SPACE to run', True, WHITE)
        runmovementOFF = menufontsmall.render('> \'C\' to stop running', True, WHITE)

        entergame = menufontsmall.render('Press ENTER to start game', True, WHITE)
        endgame = menufontsmall.render('Press ENTER to end game', True, WHITE)

        if k == 0:
            start = menufont.render('> START GAME', True, RED)
            INSTRUCTIONS = menufont.render('  INSTRUCTIONS', True, BLACK)
            controls = menufont.render('  CONTROLS', True, BLACK)
            quit = menufont.render('  QUIT GAME', True, BLACK)
            # displaying additional contents to be displayed
            screen.blit(entergame, (800, 465))

        elif k == 1:
            start = menufont.render('  START GAME', True, BLACK)
            INSTRUCTIONS = menufont.render('> INSTRUCTIONS', True, RED)
            controls = menufont.render('  CONTROLS', True, BLACK)
            quit = menufont.render('  QUIT GAME', True, BLACK)
            # displaying additional contents to be displayed
            screen.blit(controls_screen, (25, 165))
            for i in range(12):
                screen.blit(I[i], (50, 175+(24*i)))

        elif k == 2:
            start = menufont.render('  START GAME', True, BLACK)
            INSTRUCTIONS = menufont.render('  INSTRUCTIONS', True, BLACK)
            controls = menufont.render('> CONTROLS', True, RED)
            quit = menufont.render('  QUIT GAME', True, BLACK)
            # displaying additional contents to be displayed
            screen.blit(controls_screen, (25, 165))
            screen.blit(horizontalmovement, (50, 200))
            screen.blit(verticalmovement, (50, 250))
            screen.blit(bulletON, (50, 300))
            screen.blit(runmovementON, (50, 350))
            screen.blit(runmovementOFF, (50, 400))

        elif k == 3:
            start = menufont.render('  START GAME', True, BLACK)
            INSTRUCTIONS = menufont.render('  INSTRUCTIONS', True, BLACK)
            controls = menufont.render('  CONTROLS', True, BLACK)
            quit = menufont.render('> QUIT GAME', True, RED)
            # displaying additional contents to be displayed
            screen.blit(endgame, (800, 465))

        # displaying contents which should be displayed everytime
        screen.blit(Title, (415, 25))
        screen.blit(start, (700, 150))
        screen.blit(INSTRUCTIONS, (700, 225))
        screen.blit(controls, (700, 300))
        screen.blit(quit, (700, 375))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    k += 1
                    key_sound = mixer.Sound('click.wav')
                    key_sound.play()
                elif event.key == pygame.K_UP:
                    k -= 1
                    key_sound = mixer.Sound('click.wav')
                    key_sound.play()
                elif event.key == pygame.K_RETURN:
                    if k == 0:
                        key_sound = mixer.Sound('click.wav')
                        key_sound.play()
                        return True
                    elif k == 3:
                        pygame.quit()
                        sys.exit()

        k = k % 4
        pygame.display.update()

# checking for locations
def decide_location(score):
    global location
    if score < 1000:
        location = 1
    elif score in range(1000, 2000):
        location = 2
    elif score in range(2000, 4500):
        location = 3
    elif score >= 4500:
        location = 4

# Draw the Game
def player():
    global stepIndex
    if stepIndex >= 36:
        stepIndex = 0
    if move_left:
        screen.blit(left[stepIndex // 4], (playerX, playerY))
        stepIndex += 1
    elif move_right:
        screen.blit(right[stepIndex // 4], (playerX, playerY))
        stepIndex += 1
    else:
        screen.blit(playerImg, (playerX, playerY))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def obstacle(x, y, z):
    screen.blit(obstacleImg[z-1], (x, y))

def Bullet_fire(x, y):
    bullet = pygame.image.load('bullet.png')
    screen.blit(bullet, (x, y + 115))

def shoot_energyball(bX, bY):
    energyball = pygame.image.load('energy_blast.png')
    screen.blit(energyball, (bX, bY))

def enemycollide(eX, eY, pX, pY):
    if eX - pX <= 50 and pX - eX <= 30 and eY - pY <= 160 and pY - eY <= 70:
        #lost_sound = mixer.Sound('lost.wav')
        #lost_sound.play()
        return True
    return False

def obstaclecollide(oX, oY, pX, pY):
    if oX - pX <= 50 and pX - oX <= 40 and oY - pY <= 175:
        #lost_sound = mixer.Sound('lost.wav')
        #lost_sound.play()
        return True
    return False

def shoot_success(enemyX, enemyY, bulletX, bulletY):
    distanceY = enemyY - bulletY
    distanceX = enemyX - bulletX
    if distanceY < 120 and distanceY > 0 and distanceX < 1 and shoot and bulletX <= 1150:
        kill_sound = mixer.Sound('kill.wav')
        kill_sound.play()
        return True
    return False

def dodge_fail(bX, bY, pX, pY):
    distanceY = bY - pY
    distanceX = bX - pX
    if distanceX < 70 and distanceX > 20 and distanceY > 20 and distanceY < 170 and bX >= 0:
        hurt_sound = mixer.Sound('hurt.wav')
        hurt_sound.play()
        return True
    return False

if startmenu():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # selecting background for different locations
        decide_location(score)
        if (location == 1):
            bg = bg1
        elif (location == 2):
            bg = bg2
        elif (location == 3):
            bg = bg3
        elif (location == 4 and score < 9999):
            bg = bg4
        elif (location == 4 and score == 9999 and life):
            win = 1
            if i == -width:
                life = 0
                score = 10000

        # Create looping background
        screen.blit(bg, (i, 0))
        screen.blit(bg, ((width + i), 0))

        obstacle(obstacleX, obstacleY, location)

        if ballX <= 0:
            ballX = random.randint(1200, 7200)
            ballY = random.randint(160, 400)

        enemy(enemyX, enemyY)
        player()
        enemycollide(enemyX, enemyY, playerX, playerY)

        if (score >= 9950 and move_right) or (score >= 9999):
            dr_bora = pygame.image.load('enemymain.png')
            if playerX <= i + width:
                screen.blit(dr_bora, (i + width + 100, 275))
            else:
                screen.blit(dr_bora, (i + width + 100, playerY))

        if score >= 9950:
            invisisility_fading = menufontsmall.render('Dr. Bora\'s Invisibility is fading', True, WHITE)
            screen.blit(invisisility_fading, (775, 125))

        if enemyX <= -120:
            enemyX = random.randint(1200, 2400)
            enemyY = random.randint(100, 340)
        if obstacleX <= -600:
            obstacleX = random.randint(1200, 3000)
            obstacleY = 305
        if i > 0:
            i = 0
            enemyX -= 10
            obstacleX -= 10
            score += 1
        if i == -width:
            screen.blit(bg, ((width + i), 0))
            i = 0
            move_left = False

        keyinput = pygame.key.get_pressed()
        if life:
            if sprint == False:
                if keyinput[pygame.K_RIGHT]:
                    i -= 10
                    move_left = False
                    move_right = True
                    enemyX -= 20
                    obstacleX -= 10
                    if score < 9999:
                        score += 1
                elif keyinput[pygame.K_LEFT]:
                    i += 10
                    move_left = True
                    move_right = False
                    obstacleX += 10
                    if score:
                        score -= 1
                else:
                    move_left = False
                    move_right = False
                    enemyX -= 10
            if jump is False and ( keyinput[pygame.K_j] or keyinput[pygame.K_UP] ):
                jump = True
                jump_sound = mixer.Sound('jump.wav')
                jump_sound.play()

            # Jumping
            if jump is True:
                playerY -= vel_Y
                vel_Y -= 1
                if vel_Y < -20:
                    jump = False
                    vel_Y = 20

            # Firing Bullet
            if ( keyinput[pygame.K_b]):
                if shoot is False:  # If shoot is False then then the bullet may be loading or ready to fire
                    bulletY = playerY
                    shoot = True  # Bullet is fired
                    screen.blit(right[1], (playerX, playerY))
                    bullet_sound = mixer.Sound('bullet_sound.wav')
                    bullet_sound.play()

            # Bullet Movement
            if bulletX > 1200:
                bulletX = 80
                shoot = False
            if shoot is True:  # Bullet will move forward
                Bullet_fire(bulletX, bulletY)
                bulletX += vel_bul

            # sprint on
            if sprint is False and keyinput[pygame.K_SPACE]:
                sprint = True
            # sprint off
            if sprint is True and keyinput[pygame.K_c]:
                move_left = True
                sprint = False
            # sprint
            if sprint == True:
                i -= 10
                move_left = False
                move_right = True
                enemyX -= 20
                obstacleX -= 10
                if score < 9999:
                    score += 1

            shoot_energyball(ballX, ballY)
            ballX -= vel_ball

            if  dodge_fail(ballX, ballY, playerX, playerY):
                ballX = random.randint(1200, 7200)
                ballY = random.randint(160, 400)
                health -= 25
                if health <= 0:
                    life = 0
                    lost_sound = mixer.Sound('lost.wav')
                    lost_sound.play()

            if enemycollide(enemyX, enemyY, playerX, playerY) or obstaclecollide(obstacleX, obstacleY, playerX, playerY):
                if health > 0:
                    lost_sound = mixer.Sound('lost.wav')
                    lost_sound.play()
                life = 0


            if shoot_success(enemyX, enemyY, bulletX, bulletY):
                if score + 100 < 9999:
                    score += 100
                else:
                    score = 9999
                kills += 1
                bulletX = 80
                shoot = False
                enemyX = random.randint(1200, 2400)
                enemyY = random.randint(100, 340)

            # display of score
            score_font = font.render('Score : ' + str(score), True, RED)
            screen.blit(score_font, (10, 50))
            # display of location
            location_font = font.render('location : ' + str(location), True, RED)
          #  location_font_rect = location_font.get_rect()
          #  screen.blit(location_font, location_font_rect)
            screen.blit(location_font, (10, 0))
            # deisplay of health
            score_font = font.render('Health : ' + str(health) + '%', True, RED)
            screen.blit(score_font, (800, 0))
            # deisplay of kills
            score_font = font.render('Kills : ' + str(kills), True, RED)
            screen.blit(score_font, (800, 50))

        if life == 0:
            vel_ball = 0
            sprint = False
            screen.blit(bg, (i, 0))
            screen.blit(bg, ((width + i), 0))
            i -= 10
            playerX = 1200
            if score > highscore:
                highscore = score

            replay = font.render('press ENTER to play again', True, RED)
            if win and score == 10000:
                win_msg = fontbig.render(' YOU WIN ', True, RED)
                screen.blit(win_msg, (280, 150))
                if win_sound_played_once == 0:
                    win_sound = mixer.Sound('win.wav')
                    win_sound.play()
                    win_sound_played_once = 1   # the win.wav sound is played one time

            else:
                your_score = str(score)
                score_font = font.render(' Your Score : ' + your_score, True, RED)
                screen.blit(score_font, (375, 200))
                highscore_font = font.render('High Score : ' + str(highscore), True, RED)
                screen.blit(highscore_font, (375, 275))

            # replay option
            screen.blit(replay, (270, 350))

            if keyinput[pygame.K_RETURN]:
                win = 0
                win_sound_played_once = 0
                vel_ball = 25
                key_sound = mixer.Sound('click.wav')
                key_sound.play()
                kills = 0
                life = 1
                health = 100
                playerX = 50
                location = 1
                score = 0
                enemyX = random.randint(1200, 2400)
                enemyY = random.randint(100, 340)
                ballX = random.randint(1200, 7200)
                ballY = random.randint(160, 400)
                obstacleX = random.randint(1200, 3000)
                obstacleY = 305

        pygame.time.delay(15)
        pygame.display.update()
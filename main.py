import pygame
import random
from pygame import mixer

#   typing the name of all functions to be clear about which function is taken from which file. therefore not using 'from file import *'
#   all these functions are explained clearly in the files

from startmenu import startmenu
#   this file contains a function startmenu which displays the opening window along with Play, Instructions, Controls and Quit options

from decider import enemycollide, obstaclecollide, dodge_fail, decide_location, shoot_success
''' this file contains all the decider functions which decides various things such as whether Enemy, Obstacle or Energyballs collided with the
    Main player or not. also there are other decider functions which decide whether hero's bullet hit the enemies and an another one which returns
    the information about the which location the hero should be in depending on his score.  '''

from elements import player, enemy, obstacle, shoot_energyball, Bullet_fire, background_display , bora
''' this file contains functions which display the backgrounds, enemy, obstacle and the energyball attack of the enemy and the bullets used by the hero. 
    It also contains a function shoot_success which finds whether the bullet hot by the Hero is hitting the enemy or not. It also has a function
    which displays Dr. Bora at the end of the game . this usually contains functions to display all the elements of the game'''

# initialize game
pygame.init()

# window and background
screen = pygame.display.set_mode((1200, 500))

#initilizing values at the start of the game
highscore = 0 # high score initially is seeted as 0
win = 0 # this decide whether a player won or not
win_sound_played_once = 0 # this is a counter which indicates number of times win sound is played when a player wins and we could control the number of time by using this variable
kills = 0 # number of kills
life = 1 # life = 1 when the play is ON and when player loses or wins and is in game over screen then life = 0
health = 100 # health is initially 100 %
location = 1 # as game starts from location 1
# as initially the player is not moving in right , left or up direction and is not shooting any bullet the variables mentioned in the next 5 lines are initialized as false
move_left = False
move_right = False
jump = False
shoot = False
sprint = False

score = 0 # score = 0  at start of the game. ( To check the ending of the game please check with score = 9970 )

#   initializing some variables and assigning them background images
bg_img1 = pygame.image.load('location1.png')
bg1 = pygame.transform.scale(bg_img1, (1200, 500))
bg_img2 = pygame.image.load('location2.png')
bg2 = pygame.transform.scale(bg_img2, (1200, 500))
bg_img3 = pygame.image.load('location3.png')
bg3 = pygame.transform.scale(bg_img3, (1200, 500))
bg_img4 = pygame.image.load('location4.png')
bg4 = pygame.transform.scale(bg_img4, (1200, 500))
bg_list = [bg1, bg2, bg3, bg4]
#   bg_list is the list of all 4 background locations


#   initializing some variables and assigning them different fonts and colors
font = pygame.font.SysFont('forte', 50)
fontbig = pygame.font.SysFont('forte', 120)
menufont = pygame.font.SysFont('None', 80)
menufontsmall = pygame.font.SysFont('None', 40)
menufontsupersmall = pygame.font.SysFont('None', 25)
menufontbig = pygame.font.SysFont('None', 160)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)

#   initializing variables which we need
width = 1200
i = 0

# setting the game icon
pygame.display.set_caption("ROBOT WAR")
icon = pygame.image.load('gameicon.png')
pygame.display.set_icon(icon)

# Player's co-ordinates and his initial velocity in Y direction when he jumps are setted
playerX = 50
playerY = 275
vel_Y = 20

# setting Enemy's co-ordinates randomly
enemyX = random.randint(1200, 2400)
enemyY = random.randint(100, 340)

# setting Obstacle's co-ordinates where X co-ordinate is setted randomly
obstacleX = random.randint(1200, 3000)
obstacleY = 305

# Hero's Bullet co-ordinates and vel_bul in X direction
bulletX = 80
bulletY = playerY
vel_bul = 30

# setting Enemy's energy ball co-ordinates randomly and setting its velocity in horizontal direction
ballX = random.randint(1200, 7200)
ballY = random.randint(160, 400)
vel_ball = 25

if startmenu():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # when close button is clicked the game ends

        # the function decide_location returns the location hero should be in depending upon present score
        if location != decide_location(score):  # as long as the the value returned by decide_location is equal to location the appropriate background for that location is diplayed
            location = decide_location(score)   # if they both are different that indicates a location change

        # selecting different background for different locations
        bg = bg_list[location - 1]


        if (location == 4 and score == 9999 and life):
        # the player can't increase his score by killing enemies or moving forward once his score becomes 9999 when he is playing
            if i == -width:
            # the player could only increase his score to 10000 and win the game only if he touches Dr. Bora wich is possible at i = -width (line 145-148)
                win = 1 # win becomes 1 as he wins
                life = 0    # life becomes 0 as players turn of playing is complete
                score = 10000   # score becomes 10000


        # Create looping background with the background which is decided by decide_location(score) used above
        background_display(bg, i, width) # using the function looping_background which displays the looping background


        obstacle(obstacleX, obstacleY, location)    # this function displays the stationary obstacles which are lethal to the hero


        if ballX <= 0:
        # once the enemy's energy balls pass the left side of the game window they would again get reassigned random with random X and Y co-ordinates
            ballX = random.randint(1200, 7200)
            ballY = random.randint(160, 400)


        enemy(enemyX, enemyY)   # this function is used to display the enemy

        player(move_left, move_right, playerX, playerY) # this function is used to display the hero

        enemycollide(enemyX, enemyY, playerX, playerY) # this function checks whether enemy is touching the hero at any time


        if (score >= 9950 and move_right) or (score >= 9999):
            ''' when the player is moving right when his score is above 9950 he could see Dr. Bora appearing as his invisibility is fading 
            at this score(according to the story in Instructions)  and at a score of 9999 he could see Dr. Bora even if he is not moving right) '''
            bora(playerX, playerY, i, width)


        # displaying a message after score of 9950 that Dr.Bora is very close and his invisibility is fading
        if score >= 9950:
            invisisility_fading = menufontsmall.render('Dr. Bora\'s Invisibility is fading', True, WHITE)
            screen.blit(invisisility_fading, (775, 125))


        # once the enemy robot who is moving left passes through X coordinate of -120 it is again assigned some random value values for X and Y co-ordinates to attack the hero again
        if enemyX <= -120:
            enemyX = random.randint(1200, 2400)
            enemyY = random.randint(100, 340)


        # once the hero passes an obstacles successfully and moves forward such that X co-oordinate of obstacle reaches -600 then it's X co-ordinate is reassigned randomly
        if obstacleX <= -600:
            obstacleX = random.randint(1200, 3000)
            obstacleY = 305


        # when i > 0 it means that player is trying to move towards left but couldn't move left. moving left is possible only when -width < i < 0
        # this was done to correct an error in background display
        if i > 0:
            i = 0
            enemyX -= 10
            obstacleX -= 10
            score += 1


        if i == -width:
            # this part of the code is to ensure the looping of backgrounds
            screen.blit(bg, ((width + i), 0))
            i = 0
            move_left = False


        keyinput = pygame.key.get_pressed()

        if life:    # when player is playing the game
            if sprint == False: # if player is not running

                if keyinput[pygame.K_RIGHT]:    # if right arrow key is pressed
                    i -= 10 # the background moves towards left so that player moves forward in the game without actually changing his X co-ordinates
                    move_left = False
                    move_right = True
                    # move_left = False and move_right = True are passed into player function so the images of player waling right are displayed
                    enemyX -= 20    # enemy moves at speed 20 relative to the player when player is moving right
                    obstacleX -= 10 # obstacle is statinary to background so it moves with same speed as player but in opposite direction
                    if score < 9999:    # as long as the score of the player is below 9999 player could increase his score by moving forward
                        score += 1

                elif keyinput[pygame.K_LEFT]:   # if right arrow key is pressed
                    i += 10 # the background moves towards right so that player moves backward in the game without actually changing his X co-ordinates
                    move_left = True
                    move_right = False
                    # move_left = True and move_right = False are passed into player function so the images of player waling left are displaye
                    obstacleX += 10     # obstacle is statinary to background so it moves with same speed as player but in opposite direction
                    if score:
                        score -= 1  # if score is not zero(technically positive) then when player moves left his score decreases as he is moving backwards in the game
                    # in this case the relative speed between us and robot enemies is zero as both are moving left

                else:
                    # if both keys are not pressed then player appears stationary and enemy's speed is 10 towards left
                    move_left = False
                    move_right = False
                    enemyX -= 10

            # if 'J' or UP arrow key is pressed when jump is false then jump becomes true
            if jump is False and ( keyinput[pygame.K_j] or keyinput[pygame.K_UP] ):
                jump = True
                # the jump sound gets played
                jump_sound = mixer.Sound('jump.wav')
                jump_sound.play()

            # when jump is true the player jumps
            if jump is True:
                playerY -= vel_Y
                vel_Y -= 1
                if vel_Y < -20:
                    jump = False
                    vel_Y = 20

            # Firing Bullet
            if ( keyinput[pygame.K_b]):
                if shoot is False:  # If shoot is False then then the bullet is not already in motion and is ready to fire
                    bulletY = playerY
                    shoot = True  # Bullet is fired
                    # bullet firing sound is played
                    bullet_sound = mixer.Sound('bullet_sound.wav')
                    bullet_sound.play()

            # Bullet Movement
            if bulletX > 1200:
                # once bullet crosses right corner of game window without killing the enemy then it returns to us  and shoot becomes false again
                bulletX = 80
                shoot = False

            # while sjoot is true the bullet is in motion
            if shoot is True:  # Bullet will move forward
                Bullet_fire(bulletX, bulletY)
                bulletX += vel_bul # the X co-ordinate of the bullet increase with a certain speed giving the bullet motion

            # turning sprint ON
            if sprint is False and keyinput[pygame.K_SPACE]:
                sprint = True
            # turning sprint OFF
            if sprint is True and keyinput[pygame.K_c]:
                move_left = True
                sprint = False
            # when sprint is ON
            if sprint == True: # similar code to when player is moving right but this is continuous until stopped or player dies
                i -= 10
                move_left = False
                move_right = True
                enemyX -= 20
                obstacleX -= 10
                if score < 9999:
                    score += 1

            shoot_energyball(ballX, ballY) # this function is for the displaying the enemy's energyballs which reduces hero's life
            ballX -= vel_ball

            # condiion when hero gets hit by enemy's energyballs
            if  dodge_fail(ballX, ballY, playerX, playerY):
                ballX = random.randint(1200, 7200)
                ballY = random.randint(160, 400)
                health -= 25 # health reduces by 25 %
                # sound is played such that hero is hurt
                hurt_sound = mixer.Sound('hurt.wav')
                hurt_sound.play()
                if health <= 0:
                    # once his health becomes 0 he loses
                    life = 0
                    lost_sound = mixer.Sound('lost.wav')
                    lost_sound.play()

            if enemycollide(enemyX, enemyY, playerX, playerY) or obstaclecollide(obstacleX, obstacleY, playerX, playerY):
                # if hero touches enemy or obstacles then he would instantly die
                if health > 0:
                    lost_sound = mixer.Sound('lost.wav')
                    lost_sound.play()
                life = 0


            if shoot_success(enemyX, enemyY, bulletX, bulletY, shoot):
                if score + 100 < 9999:
                    # unless our score is not increasing to 10000 with that kill any kill awards the player with 100 points in score
                    score += 100
                else:
                    # if score tends to go above 9999 then is automatically becomes 9999
                    score = 9999
                kills += 1 # kills increase by 1
                bulletX = 80 # the bullet is returned to hero
                shoot = False # shoot becomes False again
                enemyX = random.randint(1200, 2400)
                enemyY = random.randint(100, 340)
                # if enemy dies then appropriate sound gets played
                kill_sound = mixer.Sound('kill.wav')
                kill_sound.play()

            # display of score
            score_font = font.render('Score : ' + str(score), True, RED)
            screen.blit(score_font, (10, 50))
            # display of location
            location_font = font.render('location : ' + str(location), True, RED)
            screen.blit(location_font, (10, 0))
            # deisplay of health
            score_font = font.render('Health : ' + str(health) + '%', True, RED)
            screen.blit(score_font, (800, 0))
            # deisplay of kills
            score_font = font.render('Kills : ' + str(kills), True, RED)
            screen.blit(score_font, (800, 50))

        if life == 0: # if life = 0  that indicates when player is presently not playing the game
            vel_ball = 0 # velocity of energy balls k=just become 0
            sprint = False # if player is sprinting that would b turned off
            background_display(bg, i, width) # appropriate background to display scores and other details is displayed
            i -= 10 # the background will be scrolling while score are displayed
            playerX = 1200
            if score > highscore:
                # if present score beats past high score it gets replaced
                highscore = score

            replay = font.render('press ENTER to play again', True, RED)
            if win:
                # if win = 1 then it means that player won and appropriate sound is played only once
                win_msg = fontbig.render(' You Win ', True, RED)
                screen.blit(win_msg, (325, 175))
                if win_sound_played_once == 0: # win_sound_played_once tells the number of times the win sound is played and this variable ensures that the sound is palyed only once
                    win_sound = mixer.Sound('win.wav')
                    win_sound.play()
                    win_sound_played_once = 1   # the win.wav sound is played one time

            else:
                # if win = 0, that means the player didn't complete the game
                btr_luck = fontbig.render(' Game Over ', True, RED)
                screen.blit(btr_luck, (275, 65))
                your_score = str(score)
                score_font = font.render(' Your Score : ' + your_score, True, RED)
                screen.blit(score_font, (375, 200))
                highscore_font = font.render('High Score : ' + str(highscore), True, RED)
                screen.blit(highscore_font, (375, 275))

            # replay option is displayed
            screen.blit(replay, (270, 350))

            if keyinput[pygame.K_RETURN]: # if ENTER key is pressed then game again starts at location 1 from the beginning and all the values are reset to how they were in location 1
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
        # screen is updated
        pygame.display.update()
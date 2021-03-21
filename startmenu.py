import pygame
import sys
from pygame import mixer

def startmenu():
    # fonts and colors
    menufont = pygame.font.SysFont('None', 80)
    menufontsmall = pygame.font.SysFont('None', 40)
    menufontsupersmall = pygame.font.SysFont('None', 25)
    menufontbig = pygame.font.SysFont('None', 160)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    screen = pygame.display.set_mode((1200, 500))

    k = 0
    while 1:
        # additional window
        controls_screen = pygame.image.load('controls_screen.png')
        # main background of startscreen and its display
        startscreen = pygame.image.load('warrobot.png')
        screen.blit(startscreen, (0, 0))

        # contents to be displayed
        Title = menufontbig.render('ROBOT WARS', True, RED)

        # contents to be displayed in Instructions
        I0 = menufontsupersmall.render('> Complete all the 4 locations and catch Dr. Bora who is hiding ', True, WHITE)
        I1 = menufontsupersmall.render('   with the help of his invisibility serum and trying to misuse ', True, WHITE)
        I2 = menufontsupersmall.render('   Dr. Vaseekaran\'s robots for his own benefits ', True, WHITE)
        I3 = menufontsupersmall.render('> Any contact with Robots or Obstacles instantly kills the Player ', True, WHITE)
        I4 = menufontsupersmall.render('   and contact with the bullets will reduce the Players\' Health.', True, WHITE)
        I5 = menufontsupersmall.render('> If the Health becomes 0 % then the Player dies.', True, WHITE)
        I6= menufontsupersmall.render('> Score, Health and number of kills along and the location can be ', True, WHITE)
        I7 = menufontsupersmall.render('   viewed on the screen.', True, WHITE)
        I8 = menufontsupersmall.render('> Score could be increased by both continuing forward in the', True, WHITE)
        I9 = menufontsupersmall.render('   game and killing the enemy robots. moving backwards in the', True, WHITE)
        I10 = menufontsupersmall.render('   game decreases the Score. ', True, WHITE)
        I11 = menufontsupersmall.render('> location change depends upon the Score', True, WHITE)
        # making a list of all these instructions
        I = [I0, I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11]

        horizontalmovement = menufontsmall.render('> Arrow keys for sideways movement', True, WHITE)
        verticalmovement = menufontsmall.render('> \'J\' (or) UP arrow key to jump', True, WHITE)

        bulletON = menufontsmall.render('> \'B\' to shoot a bullet', True, WHITE)

        runmovementON = menufontsmall.render('> SPACE to run', True, WHITE)
        runmovementOFF = menufontsmall.render('> \'C\' to stop running', True, WHITE)

        entergame = menufontsmall.render('Press ENTER to start game', True, WHITE)
        endgame = menufontsmall.render('Press ENTER to end game', True, WHITE)

        # k can have any integral value from 0-3 both inclusive
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
            # displaying additional contents( Instructions ) are displayed
            for i in range(12):
                screen.blit(I[i], (50, 175+(24*i)))

        elif k == 2:
            start = menufont.render('  START GAME', True, BLACK)
            INSTRUCTIONS = menufont.render('  INSTRUCTIONS', True, BLACK)
            controls = menufont.render('> CONTROLS', True, RED)
            quit = menufont.render('  QUIT GAME', True, BLACK)
            # displaying additional contents( Controls ) are displayed
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

        # appropriate contents are displayed for each value of k

        # displaying contents which should be displayed everytime which donot depend on the value of k
        screen.blit(Title, (415, 25))
        screen.blit(start, (700, 150))
        screen.blit(INSTRUCTIONS, (700, 225))
        screen.blit(controls, (700, 300))
        screen.blit(quit, (700, 375))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if game is quit game window closes
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # we could navigate through the 4 options on main screen with up and down arrow keys ( this is for lines 112 - 119 )
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
                        # if k = 0 when enter is pressed then the game starts
                        key_sound = mixer.Sound('click.wav')
                        key_sound.play()
                        return True
                    elif k == 3:
                        # if game is quit game window closes
                        pygame.quit()
                        sys.exit()

        k = k % 4 # if k increases above 3 then k = k % 3 ensures that it remains either 0 or 1 or 2 or 3
        pygame.display.update()
        # update the screen

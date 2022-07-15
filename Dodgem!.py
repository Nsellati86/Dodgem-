import pygame as pygame
import random
import math
import time
import sys
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE
from pygame.locals import*


def exit():
    pygame.QUIT()
    sys.exit()


def pressKeyShortcut():
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                return


def playerCrash(player_crashRect, opponent):
    for ado in opponent:

        if player_crashRect.colliderect(ado['rect']):
            return True
    return False


def txtObjects(t, f, s, x, y, txt_c):

    txt_objects = f.render(t, 1, txt_c)
    txt_Rect = txt_objects.get_rect()
    txt_Rect.topleft = (x, y)
    s.blit(txt_objects, txt_Rect)


pygame.init()
time.clock = pygame.time.Clock()
screen_display_window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Dodgem!')
pygame.mouse.set_visible(False)
fontsize = pygame.font.SysFont(None, 30)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1198, 800))

pygame.display.set_caption('Dodgem!')

logo = pygame.image.load('Dodgem!/logoAsteroid.jpg')
pygame.display.set_icon(logo)
IntroFont = pygame.font.Font("freesansbold.ttf", 38)


def introImage(x, y):
    intro = pygame.image.load("Dodgem!/gameIntro.png")
    screen.blit(intro, (x, y))


def controlsImage(x, y):
    controls = pygame.image.load("Dodgem!/gameControls.png")
    run = True

    while run:
        screen.blit(controls, (x, y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def aboutImage(x, y):
    aboutImg = pygame.image.load("Dodgem!/aboutGame.png")
    run = True

    while run:
        screen.blit(aboutImg, (x, y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def Play(x, y):
    playText = IntroFont.render("PLAY", True, (255, 0, 0))
    screen.blit(playText, (x, y))


def About(x, y):
    aboutText = IntroFont.render("ABOUT", True, (255, 0, 0))
    screen.blit(aboutText, (x, y))


def Controls(x, y):
    controlsText = IntroFont.render("CONTROLS", True, (255, 0, 0))
    screen.blit(controlsText, (x, y))


def introScreen():
    run = True
    click = False
    pygame.mixer.music.load("Dodgem!/introMusic.mp3")
    pygame.mixer.music.play()

    while run:
        screen.fill((0, 0, 0))
        introImage(0, 0)
        Play(330, 350)
        Controls(570, 350)
        About(913, 350)

        x, y = pygame.mouse.get_pos()

        button1 = pygame.Rect(300, 400, 175, 50)
        button2 = pygame.Rect(550, 400, 300, 50)
        button3 = pygame.Rect(900, 400, 165, 50)

        pygame.draw.rect(screen, (255, 255, 255), button1)
        pygame.draw.rect(screen, (255, 255, 255), button2)
        pygame.draw.rect(screen, (255, 255, 255), button3)

        if button1.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button1)
            if click:
                countdown()

        if button2.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button2)
            if click:
                controlsImage(0, 0)

        if button3.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button3)
            if click:
                aboutImage(0, 0)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85)
    countdownBackground = pygame.image.load("Dodgem!/gameBackground.png")

    three = font2.render('3', True, (187, 30, 16))
    two = font2.render('2', True, (255, 255, 0))
    one = font2.render('1', True, (51, 165, 50))
    go = font2.render('GO!!!', True, (0, 255, 0))

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()

    screen.blit(three, (500, 300))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(two, (500, 300))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(one, (500, 300))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(go, (450, 350))
    pygame.display.update()
    time.sleep(1)
    gameLoop()
    pygame.display.update()


def gameLoop():
    pygame.mixer.music.load('Dodgem!/backgroundMusic.mp3')
    pygame.mixer.music.play()
    collision_sound = pygame.mixer.Sound('Dodgem!/collisionSound.wav')
    score_value = 0
    font1 = pygame.font.Font("freesansbold.ttf", 25)

    def showScore(x, y):
        score = font1.render("SCORE: " + str(score_value), True, (255, 0, 0))
        screen.blit(score, (x, y))

    with open("Dodgem!/highscore.txt", "r") as f:
        highscore = int(f.read())

    def showHighscore(x, y):
        Hiscore_text = font1.render("HiScore: " + str(highscore), True, (255, 0, 0))
        screen.blit(Hiscore_text, (x, y))
        pygame.display.update()

    def gameOver():
        gameOverImg = pygame.image.load("Dodgem!/gameOver.png")
        run = True

        while run:
            screen.blit(gameOverImg, (0, 0))
            time.sleep(0.5)
            showScore(950, 350)
            time.sleep(0.5)
            showHighscore(950, 400)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        countdown()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    BG = pygame.image.load("Dodgem!/gameBackground.png")
    player = pygame.image.load("Dodgem!/playerShip.png")
    playerX = 350
    playerY = 495
    playerX_change = 0
    playerY_change = 0

    asteroid1 = pygame.image.load("Dodgem!/asteroid1.png")
    asteroid1X = random.randint(200, 750)
    asteroid1Y = 100
    asteroid1Ychange = 10

    asteroid2 = pygame.image.load("Dodgem!/asteroid2.png")
    asteroid2X = random.randint(200, 750)
    asteroid2Y = 100
    asteroid2Ychange = 10

    asteroid3 = pygame.image.load("Dodgem!/asteroid3.png")
    asteroid3X = random.randint(200, 750)
    asteroid3Y = 100
    asteroid3Ychange = 10

    run = True
    while run:

        for event in pygame.event.get():
            #if event.type == pygame.QUIT():
                #run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerX_change += 5

                if event.key == pygame.K_LEFT:
                    playerX_change -= 5

                if event.key == pygame.K_UP:
                    playerY_change -= 5

                if event.key == pygame.K_DOWN:
                    playerY_change += 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0

                if event.key == pygame.K_LEFT:
                    playerX_change = 0

                if event.key == pygame.K_UP:
                    playerY_change = 0

                if event.key == pygame.K_DOWN:
                    playerY_change = 0

        if playerX < 200:
            playerX = 200
        if playerX > 765:
            playerX = 765

        if playerY < 0:
            playerY = 0
        if playerY > 700:
            playerY = 700

        screen.fill((0, 0, 0,))
        screen.blit(BG, (0, 0))
        screen.blit(player, (playerX, playerY))

        screen.blit(asteroid1, (asteroid1X, asteroid1Y))
        screen.blit(asteroid2, (asteroid2X, asteroid2Y))
        screen.blit(asteroid3, (asteroid3X, asteroid3Y))

        showScore(935, 390)
        showHighscore(0, 0)

        playerX += playerX_change
        playerY += playerY_change

        asteroid1Y += asteroid1Ychange
        asteroid2Y += asteroid2Ychange
        asteroid3Y += asteroid3Ychange

        if asteroid1Y > 800:
            asteroid1Y = -100
            asteroid1X = random.randint(200, 760)
            score_value += 1
        if asteroid2Y > 800:
            asteroid2Y = -200
            asteroid2X = random.randint(200, 760)
            score_value += 1
        if asteroid3Y > 800:
            asteroid3Y = -300
            asteroid3X = random.randint(200, 760)
            score_value += 1

        if score_value > highscore:
            highscore = score_value

        def isCollision1(asteroid1X, asteroid1Y, playerX, playerY):
            distance = math.sqrt(math.pow(asteroid1X - playerX, 2) + math.pow(asteroid1Y - playerY, 2))

            if distance < 30:
                return True
            else:
                return False

        def isCollision2(asteroid2X, asteroid2Y, playerX, playerY):
            distance = math.sqrt(math.pow(asteroid2X - playerX, 2) + math.pow(asteroid2Y - playerY, 2))

            if distance < 30:
                return True
            else:
                return False

        def isCollision3(asteroid3X, asteroid3Y, playerX, playerY):
            distance = math.sqrt(math.pow(asteroid3X - playerX, 2) + math.pow(asteroid3Y - playerY, 2))

            if distance < 30:
                return True
            else:
                return False

        coll1 = isCollision1(asteroid1X, asteroid1Y, playerX, playerY)
        coll2 = isCollision2(asteroid2X, asteroid2Y, playerX, playerY)
        coll3 = isCollision3(asteroid3X, asteroid3Y, playerX, playerY)

        if coll1:
            asteroid1Ychange = 0
            asteroid2Ychange = 0
            asteroid3Ychange = 0
            asteroid1Y = 0
            asteroid2Y = 0
            asteroid3Y = 0
            playerX_change = 0
            playerY_change = 0
            pygame.mixer.music.stop()
            collision_sound.play()
            time.sleep(1)
            gameOver()

        if coll2:
            asteroid1Ychange = 0
            asteroid2Ychange = 0
            asteroid3Ychange = 0
            asteroid1Y = 0
            asteroid2Y = 0
            asteroid3Y = 0
            playerX_change = 0
            playerY_change = 0
            pygame.mixer.music.stop()
            collision_sound.play()
            time.sleep(1)
            gameOver()

        if coll3:
            asteroid1Ychange = 0
            asteroid2Ychange = 0
            asteroid3Ychange = 0
            asteroid1Y = 0
            asteroid2Y = 0
            asteroid3Y = 0
            playerX_change = 0
            playerY_change = 0
            pygame.mixer.music.stop()
            collision_sound.play()
            time.sleep(1)
            gameOver()

        if asteroid1Ychange == 0 and asteroid2Ychange == 0 and asteroid3Ychange == 0:
            pass

        with open("Dodgem!/highscore.txt", "w") as f:
            f.write(str(highscore))

        pygame.display.update()


introScreen()

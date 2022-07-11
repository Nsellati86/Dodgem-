import pygame
import random
import math
import time
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1198, 800))

pygame.display.set_caption('Dodgem!')

logo = pygame.image.load('Dodgem!/logoAsteroid.jpg')
pygame.display.set_icon(logo)

# Intro screen
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


def play(x, y):
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
        #FIXME Adjust coordinates
        play(100, 450)
        Controls(280, 450)
        About(615, 450)

        x, y = pygame.mouse.get_pos()

        #FIXME Adjust coordinates
        button1 = pygame.Rect(60, 440, 175, 50)
        button2 = pygame.Rect(265, 440, 300, 50)
        button3 = pygame.Rect(600, 440, 165, 50)

        pygame.draw.rect(screen, (255, 255, 255), button1)
        pygame.draw.rect(screen, (255, 255, 255), button2)
        pygame.draw.rect(screen, (255, 255, 255), button3)

        if button1.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button1)
            if click:
                countdown()

        if button2.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0 ), button2)
            if click:
                Controls(0, 0)

        if button3.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button3)
            if click:
                About(0, 0)

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
    #FIXME Adjust coordinates
    three = font2.render('3', True, (187, 30, 16))
    two = font2.render('2', True, (255, 255, 0))
    one = font2.render('1', True, (51, 165, 50))
    go = font2.render('GO!!!', True, (0, 255, 0))

    #FIXME Adjust coordinates
    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()

    screen.blit(three, (350, 250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(two, (350, 250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(one, (350, 250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(go, (350, 250))
    pygame.display.update()
    time.sleep(1)
    gameLoop()
    pygame.display.update()


def gameLoop():
    pygame.mixer.music.load('Dodgem!/backgroundMusic.mp3')
    pygame.mixer.music.play()
    collision_sound = pygame.mixer.Sound('Dodgem!/collisionSound.wav')
    score_value = 0
    font1 = pygame.font.Font("freesansbold.ttf, 25")

    def showScore(x, y):
        score = font1.render("SCORE: " + str(score_value), True, (255, 0, 0))
        screen.blit(score, (x, y))

    with open("Dodgem!/highscore.txt", "r") as f:
        highscore = f.read()

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
            #FIXME Adjust coordinates
            showScore(330, 400)
            time.sleep(0.5)
            showHighscore(330, 450)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.QUIT()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        countdown()
                    if event.key == pygame.K_ESCAPE:
                        pygame.QUIT()
                        sys.exit()

    BG = pygame.image.load("Dodgem!/gameBackground.png")

    player = pygame.image.load("Dodgem!/playerShip.png")
    playerX = 350
    playerY = 495
    playerX_change = 0
    playerY_change = 0

    asteroid1 = pygame.image.load("Dodgem!/asteroid1.png")
    asteroid1X = random.randint(178, 490)
    asteroid1Y = 100
    asteroidYchange = 10

    asteroid2 = pygame.image.load("Dodgem!/asteroid2.png")
    asteroid2X = random.randint(178, 490)
    asteroid2Y = 100
    asteroid2Ychange = 10

    asteroid3 = pygame.image.load("Dodgem!/asteroid3.png")
    asteroid3X = random.randint(178, 490)
    asteroid3Y = 100
    asteroid3Ychange = 10


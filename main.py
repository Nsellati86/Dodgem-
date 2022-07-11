import sys
import pygame as pygame
import time
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

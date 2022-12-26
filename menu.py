import os
import numpy as np
import random
import pygame
import sys
import math
from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes


BACKGROUND = (29, 59, 85)
BUTTON = (168, 93, 127)
RED = (251, 100, 92)


ROW_COUNT = 6
COLUMN_COUNT = 7

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu(font):
    while True:
 
        screen.fill(BACKGROUND)
        draw_text('MAKE 4', pygame.font.SysFont("monospace", 100), BUTTON, screen, 180, 40)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 200, 400, 50)
        button_2 = pygame.Rect(160, 280, 380, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.quit()
                import connect4_AI
                sys.exit()
                
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                import connect4
                sys.exit()
        pygame.draw.rect(screen, BUTTON, button_1)
        pygame.draw.rect(screen, BUTTON, button_2)
 
        draw_text('PLAYER vs AI', pygame.font.SysFont("monospace", 50), (255,255,255), screen, 170, 195)
        draw_text('MULTIPLAYER', pygame.font.SysFont("monospace", 50), (255,255,255), screen, 185, 275)


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()


pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
myfont = pygame.font.SysFont("monospace", 75)
screen = pygame.display.set_mode(size)
main_menu(myfont)

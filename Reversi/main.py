import pygame,sys,random
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()
surfrect = surface.get_rect()

rect = [[pygame.Rect((0,0),(128,128)) for i in range(8)] for j in range(8)]
for i in range(-4,4):
    for j in range(-4,4):
        rect[i+4][j+4].center = (surfrect.w/2-80*i,surfrect.h/2-80*j)

def show():
    
    surface.fill(96,96,96)
    for i in range(8):
        for j in range(8):
            
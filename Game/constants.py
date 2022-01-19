import pygame


WINDOWWIDTH = 500
WINDOWHEIGHT = 500
RATIO = WINDOWHEIGHT/WINDOWWIDTH
size = (WINDOWWIDTH, WINDOWHEIGHT)


moveSpeed = 5
mapWidth, mapHeight = 7, 7
debugging = True
dayLength = 5
framerate = 30
difficulty = 0


pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans", 24)
announcementFont = pygame.font.SysFont("Comic Sans", 72)
mathFont = pygame.font.SysFont("Comic Sans", 50)
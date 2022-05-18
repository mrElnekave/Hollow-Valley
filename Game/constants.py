import pygame


WINDOWWIDTH = 500
WINDOWHEIGHT = 500
RATIO = WINDOWHEIGHT/WINDOWWIDTH
size = (WINDOWWIDTH, WINDOWHEIGHT)
default_size = (900, 600)

player_sprite_size = 25

moveSpeed = 5
mapWidth, mapHeight = 15, 15
debugging = True
dayLength = 5
framerate = 30
difficulty = 0
start_chunk = (0, 0)


pygame.font.init()
myFont = pygame.font.SysFont("Arial", 20)
announcementFont = pygame.font.SysFont("Arial", 72)
mathFont = pygame.font.SysFont("Arial", 50)


# current_path = "Game\Data\\"
current_path = "Data\\"

reports_on = False

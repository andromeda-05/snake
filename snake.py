import pygame
import time

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

WIDTH = 500
HEIGHT = 500

screen = pygame.display.setmode((WIDTH,HEIGHT))

pygame.display.set_caption('ZMEYKA')

cur_x = WIDTH/2
cur_y = HEIGHT/2

dx = 0
dy = 0

delta = 10

flag_stop = False

clock = pygame.time.clock()

while not flag_stop:
    for event in pygame.event.get():
        if event.type == pygame.QUITE:
            flag_stop = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
        

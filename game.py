



from operator import truediv
from pickle import FALSE
import pygame
from pygame.locals import *
import time

if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    surface.fill((92,25,84))
    block = pygame.image.load("resources/block.jpg").convert()
    surface.blit(block, (50,50))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False






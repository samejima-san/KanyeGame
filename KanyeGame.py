import sys
import os
import time
import pygame
from pygame.locals import *
from Kanye import Kanye
from Zone import Zone
import random

pygame.init()

# setting up game
display_width = 800
display_height = 800
backgroundcolor = (0, 0, 0)
# win.setBackground(backgroundcolor)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dont let Kanye in his zone!')
clock = pygame.time.Clock()


# Game Running
def gameLoop():
    gameExit = False
    zone = Zone(gameDisplay)
    kanyes = []
    start = 60

    def countEnemy():
        blank = Kanye(gameDisplay)
        kanyes.append(blank)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for kanye in kanyes:
                    if kanye.kanyerect.collidepoint(pos):
                        kanye.loseHealth()
                        zone.addPoints()
                        print(zone.points)
                    if kanye.kanyerect.colliderect(zone.zonerect):
                        kanye.loseHealth()
                        zone.loseHealth()
                        print("health")
                        print(zone.health)

        pygame.display.update()
        clock.tick(60)
        start -= 1
        if start <= 0:  # spawner
            countEnemy()
            start = 45

        gameDisplay.fill(backgroundcolor)
        for kanye in kanyes:
            kanye.alive()
        zone.showZone()  # zone
        zone.displayUI()


gameLoop()
pygame.quit()

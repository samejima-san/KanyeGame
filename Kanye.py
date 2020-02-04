import pygame
import random


class Kanye():
    def __init__(self, thewindow):
        self.health = 1
        self.speed = .9
        self.kanyeImg = pygame.image.load('images/kanye.png')
        self.kanyeImg = pygame.transform.scale(self.kanyeImg, (95, 75))
        self.spawnL = random.randrange(1, 5)
        self.gameDisplay = thewindow
        if self.spawnL == 1:
            self.posx = random.randrange(0, 800)
            self.posy = 0
        elif self.spawnL == 2:
            self.posx = random.randrange(0, 800)
            self.posy = 800
        elif self.spawnL == 3:
            self.posx = 0
            self.posy = random.randrange(0, 800)
        else:
            self.posx = 800
            self.posy = random.randrange(0, 800)
        # bottom = (random, 800) right = (800, random) left = (0, random) top = (random, 0)
        self.kanyerect = self.kanyeImg.get_rect()

    def movetoplayer(self):
        # get kanye to (370,370)
        self.showKanye()
        if self.posx < 370.0:
            self.posx += self.speed
        else:
            self.posx -= self.speed
        if self.posy < 370.0:
            self.posy += self.speed
        else:
            self.posy -= self.speed
        if self.posy >= 369 and self.posx >= 369:
            self.loseHealth()

    def loseHealth(self):
        self.health -= 1
        if self.health <= 0:
            self.death()

    def death(self):
        self.kanyerect = pygame.Rect(900, 900, 0, 0)
        self.kanyeImg = None

    def showKanye(self):
        self.gameDisplay.blit(self.kanyeImg, (self.posx, self.posy))
        self.kanyerect = pygame.Rect(self.posx, self.posy, 95, 75)

    def alive(self):
        if self.health >= 1:
            self.showKanye()
            self.movetoplayer()

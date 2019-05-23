import sys, os
import time
import pygame
from pygame.locals import *
import random
pygame.init()

#setting up game
display_width = 800
display_height = 800
backgroundcolor = (0,0,0)
#win.setBackground(backgroundcolor)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dont let Kanye in his zone!')
clock = pygame.time.Clock()

class Zone():
    def __init__(self):
        self.health = 3
        self.points = 0
        self.posx = 310#(display_height * 0.34)
        self.posy = 310#(display_height * 0.34)
        self.zoneImg = pygame.image.load('images/zone.png')
        self.rect = self.image.get_rect(self.posx,self.posy)

    def takeDamage(self):
        loseHealth()
        if self.health <= 0:
            death()
    
    def addPoints(self):
        self.points += 1

    def loseHealth(self):
        self.health -= 1

    def death(self):
        self.kill()

    def displayUI(self):
        #display info
        return

    def showZone(self):
        gameDisplay.blit(self.zoneImg, (self.posx,self.posy))

class Kanye():
    def __init__(self):
        self.health = 1
        self.speed = .5
        self.kanyeImg = pygame.image.load('images/kanye.png')
        self.kanyeImg = pygame.transform.scale(self.kanyeImg, (95,75))
        self.spawnL = random.randrange(1,5)
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
        #bottom = (random, 800) right = (800, random) left = (0, random) top = (random, 0)
        self.rect = self.image.get_rect(self.posx,self.posy)

    def movetoplayer(self):
        #get kanye to (370,370)
        self.showKanye()
        if self.posx < 370.0:
           self.posx += self.speed
        else:
           self.posx -= self.speed
        if self.posy < 370.0:
           self.posy += self.speed
        else:
           self.posy -= self.speed  
        print(self.posx, self.posy)
        if self.posy >= 369 and self.posx >= 369:
            self.loseHealth()

    def loseHealth(self):
        self.health -= 1
        if self.health <= 0:
            self.death()

    def death(self):
            #figure it out dumb dumb
            return

    def showKanye(self):
        gameDisplay.blit(self.kanyeImg, (self.posx,self.posy))

    def alive(self):
       self.showKanye()
       self.movetoplayer()
        



 
#Game Running
def gameLoop():
    gameExit = False
    zone = Zone()
    kanyes = []
    start = 60
    def countEnemy():
        blank = Kanye()
        kanyes.append(blank)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            print(event)
        pygame.display.update()
        clock.tick(60) 
        start -= 1
        if start <= 0: #spawner
            countEnemy()
            start = 60
        gameDisplay.fill(backgroundcolor)
        for kanye in kanyes:
            kanye.alive()
            if kanye.is_collided_with(zone):
                kanye.kill()
        zone.showZone() #zone
        

        

        
     
       


gameLoop()
pygame.quit()
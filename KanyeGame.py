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
        self.zonerect = pygame.Rect(self.posx, self.posy, 200,200)
        self.pfont = pygame.font.SysFont('comicsans', 30, True)
        self.hfont = pygame.font.SysFont('comicsans', 30, True)
        

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
        ptext = self.pfont.render('Points: '+str(self.points),1,(255,255,255))
        gameDisplay.blit(ptext, (630,10))
        htext = self.hfont.render('Health: '+str(self.health),1,(255,255,255))
        gameDisplay.blit(htext, (100,10))

    def showZone(self):
        gameDisplay.blit(self.zoneImg, (self.posx,self.posy))

class Kanye():
    def __init__(self):
        self.health = 1
        self.speed = .9
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
        self.kanyerect = self.kanyeImg.get_rect()


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
        if self.posy >= 369 and self.posx >= 369:
            self.loseHealth()

    def loseHealth(self):
        self.health -= 1
        if self.health <= 0:
            self.death()

    def death(self):
            self.kanyerect = pygame.Rect(900, 900, 0,0)
            self.kanyeImg = None

    def showKanye(self):
        gameDisplay.blit(self.kanyeImg, (self.posx,self.posy))
        self.kanyerect = pygame.Rect(self.posx, self.posy, 95,75)

    def alive(self):
       if self.health >= 1:
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


            #print(event)
        pygame.display.update()
        clock.tick(60) 
        start -= 1
        if start <= 0: #spawner
            countEnemy()
            start = 60
        gameDisplay.fill(backgroundcolor)
        for kanye in kanyes:
            kanye.alive()
        zone.showZone() #zone
        zone.displayUI()
        
            
gameLoop()
pygame.quit()
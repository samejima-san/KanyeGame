import pygame


class Zone():
    def __init__(self, thewindow):
        self.health = 3
        self.points = 0
        self.posx = 310  # (display_height * 0.34)
        self.posy = 310  # (display_height * 0.34)
        self.zoneImg = pygame.image.load('images/zone.png')
        self.zonerect = pygame.Rect(self.posx, self.posy, 200, 200)
        self.pfont = pygame.font.SysFont('comicsans', 30, True)
        self.hfont = pygame.font.SysFont('comicsans', 30, True)
        self.gameDisplay = thewindow

    def takeDamage(self):
        self.loseHealth()
        if self.health <= 0:
            self.death()

    def addPoints(self):
        self.points += 1

    def loseHealth(self):
        self.health -= 1

    def death(self):
        self.zonerect = pygame.Rect(900, 900, 0, 0)
        self.zoneImg = None

    def displayUI(self):
        ptext = self.pfont.render(
            'Points: '+str(self.points), 1, (255, 255, 255))
        self.gameDisplay.blit(ptext, (630, 10))
        htext = self.hfont.render(
            'Health: '+str(self.health), 1, (255, 255, 255))
        self.gameDisplay.blit(htext, (100, 10))

    def showZone(self):
        self.gameDisplay.blit(self.zoneImg, (self.posx, self.posy))

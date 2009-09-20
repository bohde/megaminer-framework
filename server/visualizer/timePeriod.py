import pygame
from pygame.locals import *
from spriteClasses import Unit

class TimePeriod(object):
    def __init__(self, name, dimensions, bgcolor):
        self.color = bgcolor
        self.surface = pygame.Surface(dimensions)
        self.clearSurface()
        self.name = name
        self.objects = []
        self.presentView = ''
    
    def clearSurface(self):
       self.surface.fill(self.color)
       #pygame.display.update()
       
    def moveUnit(self, unitID, targetX, targetY):
        for unit in self.objects:
            if unit.objectID == unitID:
                self.surface.blit(unit.step, unit.rect)
                pygame.display.update()
                pygame.time.delay(500)
                unit.rect.topleft = (targetX, targetY)
                self.surface.blit(unit.stand, unit.rect)
                pygame.display.update()   
       
    def addUnit(self, statusDict):
        print "adding new unit"
        newUnit = Unit(statusDict['objectID'], statusDict['location'], statusDict['hp'],
                                  statusDict['level'], statusDict['unitType'], statusDict['ownerIndex'],
                                  statusDict['actions'], statusDict['moves'])
        self.objects.append(newUnit)
        self.surface.blit(newUnit.stand, newUnit.rect)

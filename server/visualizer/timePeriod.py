import pygame
from pygame.locals import *
from spriteClasses import Building, Unit, Terrain

class TimePeriod(object):
    def __init__(self, name, dimensions, bgcolor):
        self.color = bgcolor
        self.surface = pygame.Surface(dimensions)
        self.clearSurface()
        self.name = name
        self.units = pygame.sprite.Group()
        self.terrain = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        self.presentView = ''
    
    def clearSurface(self):
       self.surface.fill(self.color)
       #pygame.display.update()
       
       
    def updateTimePeriod(self):
        self.clearSurface()
        self.terrain.update()
        self.units.update()
        self.buildings.update()
        self.terrain.draw(self.surface)
        self.buildings.draw(self.surface)
        self.units.draw(self.surface)
       
       
    def takeStep(self, unitID):
        for unit in self.units.sprites():
            if unit.objectID == unitID:
                unit.image = unit.step
    def move(self, unitID, targetX, targetY):
        for unit in self.units.sprites():
            if unit.objectID == unitID:
                unit.image = unit.stand
                unit.rect.topleft = (targetX, targetY)
                self.updateTimePeriod()

       
    def addUnit(self, statusDict):
        print "adding new unit..."
        newUnit = Unit(statusDict['objectID'], statusDict['location'], statusDict['hp'],
                                  statusDict['level'], statusDict['unitType'], statusDict['ownerIndex'],
                                  statusDict['actions'], statusDict['moves'])
        self.units.add(newUnit)

    
    def addBuilding(self, statusDict):
        print "adding new building..."
        newBuilding = Building(statusDict['objectID'], statusDict['location'], statusDict['hp'],
                                  statusDict['level'], statusDict['buildingType'], statusDict['ownerIndex'],
                                  statusDict['inTraining'], statusDict['progress'], statusDict['linked'], statusDict['complete'])
        self.buildings.add(newBuilding)


    def addTerrain(self, statusDict):
        print "adding new terrain..."
        newTerrain = Terrain(statusDict['objectID'], statusDict['location'], statusDict['blockMove'], statusDict['blockBuild'])
        self.terrain.add(newTerrain)
        
    def remove(self, id):
        print "removing unit..."
        for unit in self.units.sprites():
            if unit.objectID == id:
                self.units.remove(unit)
        for building in self.buildings.sprites():
            if building.objectID == id:
                self.building.remove(unit)
        for terrain in self.terrain.sprites():
            if terrain.objectID == id:
                self.terrain.remove(unit)


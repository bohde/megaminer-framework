import pygame
from pygame.locals import *
from spriteClasses import Building, Unit, Terrain, loadAllImages

coordinates = {}

class TimePeriod(object):
    def __init__(self, name, pixelDim, mapDim, color):
        if not coordinates:
            self.setUp(mapDim, pixelDim)
        self.baseLayer = pygame.Surface(pixelDim)
        self.baseLayer.fill(color)
        self.terrainLayer = self.baseLayer.subsurface(self.baseLayer.get_rect()) 
        self.buildingLayer = self.baseLayer.subsurface(self.terrainLayer.get_rect())
        self.unitLayer = self.baseLayer.subsurface(self.buildingLayer.get_rect())
        self.color = color
        self.mapDim = mapDim
        self.name = name
        self.units = pygame.sprite.Group()
        self.terrain = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        self.presentView = ''
        self.drawGrass()
    
    def drawGrass(self):
        for x in range(self.mapDim[0]):
            for y in range(self.mapDim[1]):
                self.terrain.add(Terrain(None, coordinates[(x,y)], True, False))
        self.terrain.draw(self.terrainLayer)
        
    def clearGroups(self):
        self.units.clear(self.unitLayer, self.baseLayer)
        self.buildings.clear(self.buildingLayer, self.baseLayer)
        self.terrain.clear(self.terrainLayer, self.baseLayer)
       
       
    def updateTimePeriod(self):
        self.clearGroups()
        self.terrain.update()
        self.units.update()
        self.buildings.update()
        self.terrain.draw(self.baseLayer)
        self.buildings.draw(self.buildingLayer)
        self.units.draw(self.unitLayer)
       
       
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
        print "removing object..."
        for unit in self.units.sprites():
            if unit.objectID == id:
                self.units.remove(unit)
        for building in self.buildings.sprites():
            if building.objectID == id:
                self.building.remove(unit)
        for terrain in self.terrain.sprites():
            if terrain.objectID == id:
                self.terrain.remove(unit)

    def setUp(self, mapDim, pixelDim):
        xChange = int(pixelDim[0]/float(mapDim[0]))
        yChange = int(pixelDim[1]/float(mapDim[1]))

        origin = [0, pixelDim[1]/2]
        for xCoord in range(mapDim[0]):
            i = 0
            for yCoord in range(mapDim[1]):
                coordinates[(xCoord,yCoord)] = (origin[0]+i*xChange/2, origin[1]-i*yChange/2)
                i+=1

            origin[0] = origin[0] + xChange/2
            origin[1] = origin[1] + yChange/2
    
        print "xChange %(1)i ... yChange %(2)i" %{'1':xChange, '2':yChange}
        
        loadAllImages((xChange,yChange))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
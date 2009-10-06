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
        self.buildingLayer = self.terrainLayer.subsurface(self.baseLayer.get_rect())
        self.unitLayer = self.buildingLayer.subsurface(self.baseLayer.get_rect())
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
                self.terrain.add(Terrain(None, coordinates[(x,y)], False, False))
        self.terrain.draw(self.terrainLayer)
        
    def clearGroups(self):
        self.baseLayer.fill(self.color)
        self.units.clear(self.unitLayer, self.baseLayer)
        self.buildings.clear(self.buildingLayer, self.baseLayer)
        self.terrain.clear(self.terrainLayer, self.baseLayer)
       
    def updateTimePeriod(self):
        self.terrain.update()
        self.units.update()
        self.buildings.update()
        self.clearGroups()
        self.terrain.draw(self.terrainLayer)
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
                unit.faceRight = True
                self.units.update()
                unit.rect.midbottom = coordinates[(targetX, targetY)]
                self.updateTimePeriod()

       
    def addUnit(self, statusDict):
        print "adding new unit..."
        newUnit = Unit(statusDict['objectID'], coordinates[statusDict['location'][0], statusDict['location'][1]], statusDict['hp'],
                                  statusDict['level'], statusDict['unitType'], statusDict['ownerIndex'],
                                  statusDict['actions'], statusDict['moves'])
        self.units.add(newUnit)

    
    def addBuilding(self, statusDict):
        print "adding new building..."
        newBuilding = Building(statusDict['objectID'], coordinates[statusDict['location'][0], statusDict['location'][1]],
                                statusDict['hp'], statusDict['level'], statusDict['buildingType'], statusDict['ownerIndex'],
                                statusDict['inTraining'], statusDict['progress'], statusDict['linked'], statusDict['complete'])
        self.buildings.add(newBuilding)


    def addTerrain(self, statusDict):
        print "adding new terrain..."
        newTerrain = Terrain(statusDict['objectID'], coordinates[statusDict['location'][0], statusDict['location'][1]], statusDict['blockMove'], statusDict['blockBuild'])
        self.terrain.add(newTerrain)
        
    def hurt(self, id, changeHP):
        for unit in self.units.sprites():
            if unit.objectID == id:
                print "huring unit..."
                unit.hp -= changeHP
        for building in self.buildings.sprites():
            if building.objectID == id:
                print "hurting building..."
                building.hp -= changHP



    def attack(self, attackerID, targetX, targetY):
        for unit in self.units.sprites():
            if unit.objectID == attackerID:
                type = unit.unitType
                if type != 'artil' and type != 'spear' and type != 'cav':
                    raise Exception("*****You tried to attack with an invalid unitType")
                if unit.rect.midbottom[0] > coordinates[(targetX, targetY)][0]:
                    unit.image = pygame.transform.flip(unit.action, True, False)
                else:
                    unit.image = unit.action

                    
    def build(self, id, targetX, targetY):
        for unit in self.units.sprites():
            if unit.objectID == id:
                if unit.unitType != 'civE':
                    raise Exception("*****Tried to build with a non-engineer!")
                unit.working = True
            
    
                    
    def reset(self, attackerID):
        for unit in self.units.sprites():
            if unit.objectID == attackerID:
                unit.image = unit.stand
                unit.faceRight = True
                self.updateTimePeriod()
        
    def remove(self, id):
        for unit in self.units.sprites():
            if unit.objectID == id:
                print "removing unit..."
                self.units.remove(unit)
        for building in self.buildings.sprites():
            if building.objectID == id:
                print "removing building..."
                self.buildings.remove(building)
        for terrain in self.terrain.sprites():
            if terrain.objectID == id:
                print "removing terrain..."
                self.terrain.remove(terrain)


    def setUp(self, mapDim, pixelDim):
        xChange = int(pixelDim[0]/float(mapDim[0]))
        yChange = int(pixelDim[1]/float(mapDim[1]))

        origin = [xChange/2, pixelDim[1]/2]
        for xCoord in range(mapDim[0]):
            i = 0
            for yCoord in range(mapDim[1]):
                coordinates[(xCoord,yCoord)] = (origin[0]+i*xChange/2, origin[1]-i*yChange/2)
                i+=1

            origin[0] = origin[0] + xChange/2
            origin[1] = origin[1] + yChange/2
    
        print "xChange %(1)i ... yChange %(2)i" %{'1':xChange, '2':yChange}
        
        loadAllImages((xChange,yChange))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
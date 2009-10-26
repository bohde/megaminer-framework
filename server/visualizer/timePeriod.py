## @package TimePeriod
#  This is the TimePeriod class, it creates a TimePeriod, which handles most
#   of the action for the visualizer

import pygame, sys
from pygame.locals import *
from spriteClasses import Building, Unit, Terrain, loadAllImages

##  coordinates's keys are tuples for positions of the gameboard, and the values
#    correspond to the pixel position.
coordinates = {}

typeConversion = {0:'cav', 1:'art', 2:'artil', 3:'pig', 4:'spear', 5:'civE', 6:'farm', 7:'bar', 8:'school', 9:'gallery', 10:'bunk'}


## TimePeriod class
#   Each is a subview of the whole window
class TimePeriod(object):
    def __init__(self, name, pixelDim, mapDim, color):
        if not coordinates:
            self.setUp(mapDim, pixelDim)
            
        # Each type of object has a layer. Makes for easier sprite management
        self.baseLayer = pygame.Surface(pixelDim)
        self.baseLayer.fill(color)
        self.terrainLayer = self.baseLayer.subsurface(self.baseLayer.get_rect()) 
        self.buildingLayer = self.terrainLayer.subsurface(self.baseLayer.get_rect())
        self.unitLayer = self.buildingLayer.subsurface(self.baseLayer.get_rect())
        self.countLayer = self.unitLayer.subsurface(self.baseLayer.get_rect())
        # SpaceOccupation keeps track of how many units are on each space
        self.spaceOccupation = {}
        for key, loc in coordinates.iteritems():
            self.spaceOccupation[loc] = 0
        self.color = color
        self.mapDim = mapDim
        self.name = name
        self.grass = pygame.sprite.Group()
        self.units = pygame.sprite.Group()
        self.terrain = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        self.presentView = ''
        self.drawGrass()
    
    ##Draws ONLY grass, to be blitted when screen is redrawn
    def drawGrass(self):
        for x in range(self.mapDim[0]):
            for y in range(self.mapDim[1]):
                self.grass.add(Terrain(None, coordinates[(x,y)], False, False))
        self.grass.draw(self.baseLayer)
        
    ##clears the screen for the next frame
    def clearGroups(self):
        self.baseLayer.fill(self.color)
        self.grass.draw(self.baseLayer)
        self.units.clear(self.unitLayer, self.baseLayer)
        self.buildings.clear(self.buildingLayer, self.baseLayer)
        self.terrain.clear(self.terrainLayer, self.baseLayer)
      
    ## redraws each subsurface and updates all sprites 
    def updateTimePeriod(self):
        self.clearGroups()
        self.terrain.update()
        self.units.update()
        self.buildings.update()
        self.terrain.draw(self.terrainLayer)
        self.buildings.draw(self.buildingLayer)
        self.units.draw(self.unitLayer)
        for key, count in self.spaceOccupation.iteritems():
            if count > 1:
                print "period %s" %self.name
                font = pygame.font.Font(None, 24)
                text = font.render("2", 1, (250,250,250))
                textloc = text.get_rect()
                textloc.midbottom = key
                self.countLayer.blit(text, textloc)
                pygame.display.update()

    ## takeStep and move are called in order to make a unit move animated-ly
    def takeStep(self, unitID):
        for unit in self.units.sprites():
            if unit.objectID == unitID:
                unit.stepping = True
                self.spaceOccupation[unit.rect.midbottom]-=1
    def move(self, unitID, targetX, targetY):
        for unit in self.units.sprites():
            if unit.objectID == unitID:
                print "  TYPE: ", unit.unitType
                unit.stepping = False
                unit.faceRight = True
                self.units.update()
                unit.rect.midbottom = coordinates[(targetX+10, targetY+10)]
                self.updateTimePeriod()
                self.spaceOccupation[unit.rect.midbottom]+=1
                print "The space count is %i" %self.spaceOccupation[unit.rect.midbottom]

    ## adds a unit to the Unit sprite group
    def addUnit(self, statusDict):
        print "adding new unit...", statusDict['objectID']
        try:
            self.spaceOccupation[coordinates[(statusDict['location'][0]+10, statusDict['location'][1]+10)]]+=1
        except:
            sys.exit("HotDogDanceParty")
        newUnit = Unit(statusDict['objectID'], coordinates[statusDict['location'][0]+10, statusDict['location'][1]+10], statusDict['hp'],
                                  statusDict['level'], typeConversion[statusDict['unitType']], statusDict['ownerIndex'],
                                  statusDict['actions'], statusDict['moves'])
        self.units.add(newUnit)
            

    ## adds a building to the building sprite group
    def addBuilding(self, statusDict):
        print "adding new building..."
        newBuilding = Building(statusDict['objectID'], coordinates[statusDict['location'][0]+10, statusDict['location'][1]+10],
                                statusDict['hp'], statusDict['level'], typeConversion[statusDict['buildingType']], statusDict['ownerIndex'],
                                statusDict['inTraining'], statusDict['progress'], statusDict['linked'], statusDict['complete'])

        self.buildings.add(newBuilding)

    ## adds terrain to the terrain sprite group
    def addTerrain(self, statusDict):
        print "adding new terrain..."
        newTerrain = Terrain(statusDict['objectID'], coordinates[statusDict['location'][0]+10, statusDict['location'][1]+10], statusDict['blockMove'], statusDict['blockBuild'])
        self.terrain.add(newTerrain)
        
    ## applies damage to an object
    def hurt(self, id, changeHP):
        for unit in self.units.sprites():
            if unit.objectID == id:
                print "huring unit..."
                unit.hp -= changeHP
        for building in self.buildings.sprites():
            if building.objectID == id:
                print "hurting building..."
                building.hp -= changHP


    ## animates an object and causes it to attack
    def attack(self, attackerID, targetX, targetY):
        for unit in self.units.sprites():
            if unit.objectID == attackerID:
                if unit.unitType != 'artil' and type != 'spear' and type != 'cav':
                    raise Exception("*****You tried to attack with an invalid unitType")
                unit.attacking = True

    ## sets a civE to begin building ALSO stops the building process by calling it on the same objID
    def build(self, id, targetX, targetY):
        for unit in self.units.sprites():
            if unit.objectID == id:
                if unit.unitType != 'civE':
                    raise Exception("*****Tried to build with a non-engineer!")
                if unit.working == False:
                    unit.working = True
                    print "unit has begun building..."
                else:
                    unit.working = False
                    print "unit has stopped building..."
        
    ## removes an object entirely
    def remove(self, id):
        for unit in self.units.sprites():
            if unit.objectID == id:
                print "removing unit..."
                self.units.remove(unit)
                self.spaceOccupation[unit.rect.midbottom]-=1
        for building in self.buildings.sprites():
            if building.objectID == id:
                print "removing building..."
                self.buildings.remove(building)
        for terrain in self.terrain.sprites():
            if terrain.objectID == id:
                print "removing terrain..."
                self.terrain.remove(terrain)

    ## sets a building to animate training
    def train(self, id):
        for building in self.buildings.sprites():
            if building.objectid == id:
                building.training = True
                
    ## stops animating training and sets unitType images
    def stopTrain(self, id):
        for building in self.buildingss.sprites():
            if building.objectid == id:
                building.training = False

    ## sets up coordinate dictionary for easier map->pixel coordinate conversions
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
        '''
        for xCoord in range(-10,11,1):
            i = 0
            for yCoord in range(-10,11,1):
                j = 0
                coordinates[(xCoord,yCoord)] = tempCoords[(i,j)]
        '''
        
        print "Coordinates: "
        for key, value in coordinates.iteritems():
            print "  Map: ", key, " Pixel: ", value
    
        print "xChange %(1)i ... yChange %(2)i" %{'1':xChange, '2':yChange}
        
        loadAllImages((xChange,yChange))
        

import pygame, os
from pygame.locals import *
from spriteClasses import Unit
from timePeriod import TimePeriod

windowDimensions = (1280,1024)
viewDimensions={"l":{"dimensions":(1280, 640), "upperLeftCorner":(0, 0)},
                "s1":{"dimensions":(608, 342), "upperLeftCorner":(0, 682 )},
                "s2":{"dimensions":(608, 342), "upperLeftCorner":(672, 682)}}
periodNames = {'farPast':[100,0,0], 'past':[0,100,0], 'present':[0,0,100]}
periodDimensions = (20,20)
grassColor = [0,123,12]
background = pygame.image.load(os.path.join("sprites", "background.jpg"))

class Window(object):
    def __init__(self):
        self.status = {}
        self.colorIndex = 0
        self.views = {}
        self.timePeriods = {}
        self.display = pygame.display.set_mode(windowDimensions)
        #self.display.blit(background, self.display.get_rect())
        self.setUpTimePeriods()
        #self.objects = []
        pygame.display.update()
        
    def setUpTimePeriods(self):
        for name, color in periodNames.iteritems():
            self.timePeriods[name] = TimePeriod(name, viewDimensions['l']['dimensions'], periodDimensions, color)
        self.timePeriods['farPast'].presentView = 's2'
        self.timePeriods['past'].presentView = 'l'
        self.timePeriods['present'].presentView = 's1'
        self.createSubViews()
    
    def createSubViews(self):
        for name, dict in viewDimensions.iteritems():
            rectangle = pygame.Rect(dict["upperLeftCorner"], dict["dimensions"])
            self.views[name] = self.display.subsurface(rectangle)
        self.updateScreen()

    def clearTimePeriodSurfaces(self):
        for name, item  in self.timePeriods.iteritems():
            item.clearSurface()
            
    def focusOn(self, focusPeriod):
        print "changing focus..."
        oldView = self.timePeriods[focusPeriod].presentView
        print oldView
        for name, period in self.timePeriods.iteritems():
            if period.presentView == 'l':
                print "found large view"
                pygame.transform.scale(period.surface, viewDimensions[oldView]['dimensions'], self.views[oldView])
                pygame.transform.scale(self.timePeriods[focusPeriod].surface, viewDimensions['l']['dimensions'], self.views['l'])
        pygame.display.update()

    def updateScreen(self):
        for name, period in self.timePeriods.iteritems():
            period.updateTimePeriod()
            pygame.transform.scale(period.baseLayer, viewDimensions[period.presentView]['dimensions'], self.views[period.presentView])
        pygame.display.update()

    def add(self, id):
        for period, dictionary in self.status.iteritems():
            for type, list in dictionary.iteritems():
                for item in list:
                    if item['objectID'] == id:
                        if type == 'Unit':
                            self.timePeriods[period].addUnit(item)
                        if type == 'Building':
                            self.timePeriods[period].addBuilding(item)
                        if type == 'Terrain':
                            self.timePeriods[period].addTerrain(item)
                            
    def remove(self, id):
        for name, period in self.timePeriods.iteritems():
            period.remove(id)
    
    def move(self, id, targetX, targetY):
        print "moving unit..."
        for name, period in self.timePeriods.iteritems():
            period.takeStep(id)
            self.updateScreen()
            pygame.time.delay(250)
            period.move(id, targetX, targetY)
            self.updateScreen()
    
    def attack(self, attackerID, targetX, targetY):
        for period, dictionary in self.status.iteritems():
            for type, list in dictionary.iteritems():
                for item in list:
                    if item['objectID'] == id:
                        if type == 'Unit':
                            self.timePeriods[period].attackUnit(item)
    
    def hurt(self, id, changeHP):
        for period, dictionary in self.status.iteritems():
            for type, list in dictionary.iteritems():
                for item in list:
                    if item['objectID'] == id:
                        if type == 'Unit':
                            self.timePeriods[period].hurtUnit(item)
                        if type == 'Building':
                            self.timePeriods[period].hurtBuilding(item)
                        if type == 'Terrain':
                            self.timePeriods[period].hurtTerrain(item)
    
    def build(self, id, targetX, targetY):
        for period, dictionary in self.status.iteritems():
            for type, list in dictionary.iteritems():
                for item in list:
                    if item['objectID'] == id:
                        if type == 'Building':
                            self.timePeriods[period].build(item)
    
    def train(self, id, newUnitTypeID):
        for period, dictionary in self.status.iteritems():
            for type, list in dictionary.iteritems():
                for item in list:
                    if item['objectID'] == id:
                        if type == 'Unit':
                            self.timePeriods[period].trainUnit(item)
    
    def updateStatus(self, newStatus):
        self.status = newStatus

    """
    #just to help identify each view.
    def color(self):
        if self.colorIndex == 0:
            self.colorIndex += 1
            return [100,0,0]
        if self.colorIndex == 1:
            self.colorIndex += 1 
            return [0,0,100]
        else:
            return grassColor
       """ 

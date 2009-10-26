## @package Window
#  This is the window class, it creates a window and mainains all its contents

import pygame, os
from pygame.locals import *
from spriteClasses import Unit
from timePeriod import TimePeriod

## Global variables for Window
windowDimensions = (1280,1024)

#Dimensions of Subviews
viewDimensions={"l":{"dimensions":(1280, 640), "upperLeftCorner":(0, 0)},
                "s1":{"dimensions":(608, 342), "upperLeftCorner":(0, 682 )},
                "s2":{"dimensions":(608, 342), "upperLeftCorner":(672, 682)}}

#Period names as well as default background colors
periodNames = {'farPast':[100,0,0], 'past':[0,100,0], 'present':[0,0,100]}

#Period dimensions, in terms of map, a 10 by 10 map would be (10,10)
periodDimensions = (20,20)

#Delay time between frams. In milliseconds
delaytime = 250

##This class defines the window object. Visualizer protocol
# calls methods on the window object to change the state of the
# visualizer
class Window(object):
    ## sets up Window object
    def __init__(self):
        pygame.init()
        self.status = {}
        self.views = {}
        self.timePeriods = {}
        self.display = pygame.display.set_mode(windowDimensions)
        self.setUpTimePeriods()
        pygame.display.update()
        
    ## initializes 3 TimePeriod objects and gives them their initial subview name
    def setUpTimePeriods(self):
        for name, color in periodNames.iteritems():
            self.timePeriods[name] = TimePeriod(name, viewDimensions['l']['dimensions'], periodDimensions, color)
        self.timePeriods['farPast'].presentView = 's1'
        self.timePeriods['past'].presentView = 'l'
        self.timePeriods['present'].presentView = 's2'
        self.createSubViews()
    
    ## creates subviews on the display for the TimePeriods to be drawn in
    def createSubViews(self):
        for name, dict in viewDimensions.iteritems():
            rectangle = pygame.Rect(dict["upperLeftCorner"], dict["dimensions"])
            self.views[name] = self.display.subsurface(rectangle)
        self.updateScreen()

    ## iterates through created TimePeriods and clears the surfaces
    #  usually prior to re-drawing screen
    def clearTimePeriodSurfaces(self):
        for name, item  in self.timePeriods.iteritems():
            item.clearGroups()
            
    ## changes the largest subview so that focus is changed to requested
    #  timeperiod
    # @param focusPeriod- the name of the requested TimePeriod (i.e. 'past')
    def focusOn(self, focusPeriod):
        print "changing focus..."
        oldView = self.timePeriods[focusPeriod].presentView
        print "*%(1)s" %{'1':oldView}
        for name, period in self.timePeriods.iteritems():
            if period.presentView == 'l':
                print "*found large view"
                period.presentView = oldView
                self.timePeriods[focusPeriod].presentView = 'l'
        self.updateScreen()

    ## instead of calling pygame.display.update(), call this to update all
    #  TimePeriods and their subviews
    def updateScreen(self):
        for name, period in self.timePeriods.iteritems():
            period.updateTimePeriod()
            pygame.transform.scale(period.baseLayer, viewDimensions[period.presentView]['dimensions'], self.views[period.presentView])
        pygame.time.delay(delaytime)
        pygame.display.update()


    ## iterates through the status to find the requested id, and it to the
    #  appropriate sprite group and TimePeriod
    # @param id- an objectID (int)
    def add(self, id):  
        print "looking for ", id
        for period, dictionary in self.status.iteritems():
            for type, list in dictionary.iteritems():
                for item in list:
                    if item['objectID'] == id:
                        print "  adding ", id
                        if type == 'Unit':
                            self.timePeriods[period].addUnit(item)
                        if type == 'Building':
                            self.timePeriods[period].addBuilding(item)
                        if type == 'Terrain':
                            self.timePeriods[period].addTerrain(item)
                            
        self.updateScreen()
                        
    ## remove(self, id)
    #  iterates through TimePeriods, calling each period's remove method
    #  to remove the requested object
    def remove(self, id):
        for name, period in self.timePeriods.iteritems():
            period.remove(id)
    
    ## moves the object with objectID "id" to the requested x,y coordinate
    #  @param id- an objectID; targeX/Y- target coords. (all are ints)
    def move(self, id, targetX, targetY):
        print "moving unit..."
#        if targetX >= periodDimensions[0] or targetY >= periodDimensions[1]:
#            raise Exception("**********Tried moving outside of range")
        for name, period in self.timePeriods.iteritems():
            period.takeStep(id)
            self.updateScreen()
            period.move(id, targetX, targetY)
            self.updateScreen()
    
    ## calls attack and reset for the requested ID to each TimePeriod
    #  this causes the object to strike in the direction of the target, but
    #  does NOT cause it to move to (targetX,targetY)
    #  @param attackerID- objectID; targetX/Y- target coords (all ints)
    def attack(self, attackerID, targetX, targetY):
        print "attacking...."
        for name, period in self.timePeriods.iteritems():
            period.attack(attackerID, targetX, targetY)
            self.updateScreen()
    
    ## calls hurt on each TimePeriod for id, "id's" hp is then decremented
    #  by changeHP
    # @param id- an object id (int); changeHP- the change in hp, (+ hurt, - heal)
    def hurt(self, id, changeHP):
        for name, period in self.timePeriods.iteritems():
            period.hurt(id, changeHP)
    
    ## causes a civil engineer "id" to swing its pickaxe in the direction
    #  of target.
    # @param id- object id (int); targetX/targetY- requested coords (ints)
    def build(self, id, targetX, targetY):
        for name, period in self.timePeriods.iteritems():
            period.build(id, targetX, targetY)
    
    ## trains a unit to be a certain type of unit
    # @param
    def train(self, id, newUnitTypeID):
        for name, period in self.timePeriods.iteritems():
            period.train(id)
    
    ## replaces old status dictionary with newStatus
    # @param newStatus- a status dictionary.
    def updateStatus(self, newStatus):
        self.status.update(newStatus)

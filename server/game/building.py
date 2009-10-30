from hittableObject import *
import unit
import math

class Building(HittableObject):
    def __init__(self, game, x, y, z, owner, type, level):
        HittableObject.__init__(self, game, x, y, z, type, level)
        self.type = type
        self.training = None #The type of unit in progress, or None
        self.progress = 0 #The number of turns spent training
        self.owner = owner
        self.linked = False #True if this building also exists in a future era
        self.complete = False

    def toList(self):
        list = HittableObject.toList(self)
        if (self.training is not None):
            inTraining = self.training.id
        else:
            inTraining = -1
        ownerIndex = self.game.players.index(self.owner)
        list.extend([self.level, self.type.id, ownerIndex, inTraining, 
                     self.progress, 1 * self.linked, 1 * self.complete])
        return list

    def bringToCompletion(self):
        if (not self.complete):
            self.complete = True
            self.hp = self.type.effHP(self.level)
            #Cascade through time
            if (self.z < 2):
                #Check future terrain
                for coord in self.coveredArea():
                    terrain = self.game.getTerrain(coord[0],coord[1],self.z+1)
                    portal = self.game.getPortal(coord[0], coord[1], self.z+1)
                    if (terrain is not None and terrain.blockBuild):
                        return
                    if (portal is not None):
                        return
                #Kill enemies in the way
                for coord in self.coveredArea():
                    enemies = self.game.getEnemies(coord[0],coord[1],self.z+1)
                    for e in enemies:
                        e.takeDamage(self.hp, True)
                    building = self.game.getBuilding(coord[0],coord[1],self.z+1)
                    if building is not None:
                        building.takeDamage(self.hp, True)
                newBuilding = Building(self.game, self.x, self.y, self.z + 1,\
                                   self.owner, self.type, self.level + 1)
                self.game.addObject(newBuilding)
                newBuilding.bringToCompletion()
                self.linked = True

    def addToMap(self):
        for x in xrange(self.x, self.x + self.type.width):
            for y in xrange(self.y, self.y + self.type.height):
                self.game.periods[self.z].area[(x, y)].append(self)
        if (self.game.turn is None):
            #buildings placed before the start of the game are complete
            self.bringToCompletion()
        else:
            self.hp = 0
            self.beBuilt()

    def removeFromMap(self):
        if (self.z > 0):
            pastSelf = self.game.getBuilding(self.x, self.y, self.z-1)
            if (pastSelf is not None):
                pastSelf.linked = False
        if (self.linked):
            futureSelf = self.game.getBuilding(self.x, self.y, self.z+1)
            self.game.removeObject(futureSelf)
        for x in xrange(self.x, self.x + self.type.width):
            for y in xrange(self.y, self.y + self.type.height):
                self.game.periods[self.z].area[(x, y)].remove(self)

    def nextTurn(self):
        HittableObject.nextTurn(self)
        if (self.training is not None):
            if (self.game.turn == self.owner):
                self.progress += 1
                #Removed so that changed list only reflects new units
                #self.changed = True
            if (self.progress >= self.training.trainTime):
                newUnit = unit.Unit(self.game, self.x + self.type.spawnX,
                               self.y + self.type.spawnY, self.z, \
                               self.owner, self.training, 0)
                self.game.addObject(newUnit)
                self.training = None
                self.progress = 0

    def beBuilt(self):
        """
        Increases this building's hp based on the amount of time required to
        build it.
        """
        self.hp += math.ceil(self.type.effHP(self.level) * 
                     (1.0 / self.type.buildTime[self.z]))
        self.hp = int(min(self.hp, self.type.effHP(self.level)))
        #Removed so that changed list only reflects new units
        #self.changed = True
        if (not self.complete and self.hp == self.type.effHP(self.level)):
            self.bringToCompletion()

    def train(self, newUnitType):
        """
        Begin training the desired unit type
        """
        if (not self.game.turn == self.owner):
            return str(self.id) + " is not your building"
        if (newUnitType.trainedBy != self.type):
            return str(self.id) + " can not train that type"
        if (self.training is not None):
            return str(self.id) + " is already training a unit"
        if (self.owner.gold[self.z] < newUnitType.price):
            return "You can not afford to train this unit"
        if (not self.complete):
            return str(self.id) + " can not train until completed"
        self.game.animations += [["train", self.id, newUnitType.id]]
        self.training = newUnitType
        self.progress = 0
        self.owner.gold[self.z] -= newUnitType.effPrice(self.level)
        #Removed so that changed list only reflects new units
        #self.changed = True
        return True

    def cancel(self):
        """
        If this building is not complete, cancels construction of this
          building.  Otherwise, attempts to cancel training.
        """
        if (not self.game.turn == self.owner):
            return str(self.id) + " is not your building"
        if (self.complete == True):
            if (self.training is None):
                return str(self.id) + " is complete not training anything."
            #Cancel training
            self.progress = 0
            self.owner.gold[self.z] += self.training.effPrice(self.level)
            self.training = None
            self.game.animations += [["stopTrain", self.id]]
        else:
            #Cancel construction of this building
            self.owner.gold[self.z] += self.type.effPrice(self.level)
            self.game.animations += [["cancel", self.id]]
            self.game.removeObject(self)
        return True

    def adjArea(self):
        """
        Returns a set of tuples (x,y) that are considered adjacent to this
          building
        """
        return self.type.adjArea(self.x, self.y)

    def coveredArea(self):
        """
        Returns a set of tuples (x,y) that are covered by this building
        """
        return self.type.coveredArea(self.x, self.y)


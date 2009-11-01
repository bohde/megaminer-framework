from hittableObject import *
from building import Building

class Unit(HittableObject):
    """
    Any object that is owned by a player and can move inherits from this class.
    This class handles functions related to attacking and moving.
    """

    def __init__(self, game, x, y, z, owner, type, level):
        HittableObject.__init__(self, game, x, y, z, type, level)
        self.hp = self.type.effHP(self.level)
        self.actions = 0
        self.moves = 0
        self.owner = owner
        self.type = type

    def toList(self):
        list = HittableObject.toList(self)
        ownerIndex = self.game.players.index(self.owner)
        list.extend([self.level, self.type.id, ownerIndex, self.actions, 
                     self.moves])
        return list

    def nextTurn(self):
        HittableObject.nextTurn(self)
        if (self.owner == self.game.turn):
            self.actions = self.type.actions
            self.moves = self.type.moves
            #Removed so that changed list only reflects new units
            #changed = True

    def move(self, targetX, targetY):
        dis = self.game.distance(self.x, self.y, targetX, targetY)
        if (not self.owner == self.game.turn):
            return str(self.id) + " does not belong to you"
        if (self.moves < 1):
            return str(self.id) + " is out of moves"
        if (dis != 1):
            return str(self.id) + " can only move to adjacent squares"
        myPeriod = self.game.periods[self.z]
        if (not myPeriod.area.inBounds(targetX, targetY)):
            return str(self.id) + " can not move off the map"
        terrain = self.game.getTerrain(targetX, targetY, self.z)
        if (terrain is not None):
            if (terrain.blockMove):
                return str(self.id) + " ran into a mountain"
        if (self.game.getEnemies(targetX, targetY, self.z)):
            return str(self.id) + " ran into an enemy unit or building"
        self.removeFromMap()
        self.x = targetX
        self.y = targetY
        self.moves -= 1
        self.game.animations += [["move", self.id, targetX, targetY]]
        #Removed so that changed list only reflects new units
        #self.changed = True
        self.addToMap()
        return True

    def warp(self):
        if (not self.owner == self.game.turn):
            return str(self.id) + " does not belong to you"
        portal = self.game.getPortal(self.x, self.y, self.z)
        if (portal is None):
            return str(self.id) + " can not warp without a portal"
        errBuff = portal.chargeToll(self.owner)
        if (errBuff != True):
            return errBuff
        self.removeFromMap()
        self.z += portal.direction
        self.game.animations += [["warp", self.id, self.z]]
        #Kill all enemies in the way
        squatters = self.game.getEnemies(self.x, self.y, self.z)
        for obj in squatters:
            obj.takeDamage(obj.hp, True)
        #Removed so that changed list only reflects new units
        #self.changed = True
        self.addToMap()
        return True


    def attack(self, targetX, targetY):
        """
        This unit attacks the target coordinate.
        If there is a completed building there, it takes the damage and 
          all other units there go unharmed.
        If there is no completed building there, the full damage hits each unit
          and building in the target coordinate.
        """
        if (not self.owner == self.game.turn):
            return str(self.id) + " does not belong to you"
        myPeriod = self.game.periods[self.z]
        if (not myPeriod.area.inBounds(targetX, targetY)):
            return str(self.id) + " can not attack off the map"
        if (self.actions < 1):
            return str(self.id) + " is out of actions"
        if (self.moves < self.type.attackCost):
            return str(self.id) + " has insufficient moves"
        dis = self.game.distance(self.x, self.y, targetX, targetY)
        if (dis > self.type.maxRange):
            return str(self.id) + " is out of range of " + str(targetX) \
                   + ", " + str(targetY)
        if (dis < self.type.minRange):
            return str(self.id) + " is inside the min range of " \
                   + str(targetX) + ", " + str(targetY)
        self.game.animations += [["attack", self.id, targetX, targetY]]
        shelter = self.game.getBuilding(targetX, targetY, self.z)
        if (shelter is not None and shelter.complete):
            shelter.takeDamage(self.type.effDamage(self.level))
        else:
            for target in self.game.periods[self.z].area[(targetX, targetY)]:
                if isinstance(target, HittableObject):
                    target.takeDamage(self.type.effDamage(self.level))
        self.actions -= 1
        self.moves -= self.type.attackCost
        #Removed so that changed list only reflects new units
        #self.changed = True
        return True





    def paint(self, targetX, targetY):
        if (not self.owner == self.game.turn):
            return str(self.id) + " does not belong to you"
        if (self.actions < 1):
            return str(self.id) + " is out of actions"
        dis = self.game.distance(self.x, self.y, targetX, targetY)
        if (dis > 1):
            return str(self.id) + " is not adjacent to target gallery"
        gallery = self.game.getBuilding(targetX, targetY, self.z)
        if (gallery is None):
            return str(self.id) + " tried to paint the ground"
        if (not gallery.type.allowPaint):
            return str(self.id) + " tried to paint an invalid building"
        if (not self.type.canPaint):
            return str(self.id) + " can not paint"
        self.game.animations += [["paint", self.id, targetX, targetY]]
        artWorth = self.type.artWorth(self.level, gallery.level)
        self.owner.gold[self.z] += artWorth
        self.actions -= 1
        #Removed so that changed list only reflects new units
        #self.changed = True
        return True

    def build(self, targetX, targetY, buildingType=None):
        """
        Attempts to construct the desired building, or continues the building
        already at that location if no type is specified.
        """
        if (not self.owner == self.game.turn):
            return str(self.id) + " does not belong to you"
        if (self.actions < 1):
            return str(self.id) + " is out of actions"
        if (self.game.getEnemies(targetX, targetY, self.z)):
            return str(self.id) + " can not build on enemy units or buildings"
        existingBuilding = self.game.getBuilding(targetX, targetY, self.z)
        if (buildingType is None or existingBuilding is not None):
            if (not (self.x,self.y) in existingBuilding.adjArea()):
                return str(self.id) + " is not adjacent to that building"
            if (existingBuilding is None):
                return str(self.id) + " tried to build nothing"
            if (existingBuilding.type.builtBy != self.type):
                return str(self.id) + " can not continue construction on" \
                                    + " that type"
            existingBuilding.beBuilt()
        else:
            if (existingBuilding is not None):
                return str(self.id) + " tried to build on top of a building"
            if (not(self.x, self.y)in buildingType.adjArea(targetX, targetY)):
                return str(self.id) + "is not adjacent to new building"
            for coord in buildingType.coveredArea(targetX, targetY):
                terrain = self.game.getTerrain(coord[0], coord[1], self.z)
                if (terrain is not None and terrain.blockBuild):
                    return str(self.id) + " can not build on a mountain"
                portal = self.game.getPortal(coord[0], coord[1], self.z)
                if (portal is not None):
                    return str(self.id) + " can not build on a portal"
            for coord in buildingType.coveredArea(targetX, targetY):
                if not self.game.periods[self.z].area.inBounds(coord[0], 
                                                                coord[1]):
                    return str(self.id) + " can not build out of bounds"
            if (buildingType.builtBy != self.type):
                return str(self.id) + " can not construct that type"
            if (self.owner.gold[self.z] < buildingType.price):
                return "You do not have enough gold to build that"
            self.game.animations += [["build", self.id, targetX, targetY]]
            newBuilding = Building(self.game, targetX, targetY, self.z, \
                                   self.owner, buildingType, self.level)
            self.game.addObject(newBuilding)
            self.owner.gold[self.z] -= buildingType.price
        return True



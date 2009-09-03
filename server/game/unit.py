from hittableObject import *
from building import *

class Unit(HittableObject):
    """
    Any object that is owned by a player and can move inherits from this class.
    This class handles functions related to attacking and moving.
    """
    def __init__(self, game, x, y, z, owner, type):
        HittableObject.__init__(self, game, x, y, z, type)
        self.hp = type.hp
        self.actions = 0
        self.moves = 0
        self.owner = owner
        self.type = type
        self.level = 1

    def toList(self):
        list = HittableObject.toList(self)
        ownerIndex = self.game.players.index(self.owner)
        list.extend([self.level, self.type.id, ownerIndex, self.actions, 
                     self.moves])
        return list

    def nextTurn(self):
        HittableObject.nextTurn(self)
        self.actions = self.type.actions
        self.moves = self.type.moves

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
        self.removeFromMap()
        self.x = targetX
        self.y = targetY
        self.moves -= 1
        self.game.animations += [["move", self.id, targetX, targetY]]
        self.changed = True
        self.addToMap()
        return True

    def attack(self, targetX, targetY):
        if (not self.owner == self.game.turn):
            return str(self.id) + " does not belong to you"
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
        for target in self.game.periods[self.z].area[(targetX, targetY)]:
            target.takeDamage(self.type.damage)
        self.actions -= 1
        self.moves -= self.type.attackCost
        self.changed = True
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
        self.owner.gold += 10
        self.actions -= 1
        self.changed = True
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
        dis = self.game.distance(self.x, self.y, targetX, targetY)
        if (dis > 1):
            return str(self.id) + " must be adjacent to build"
        existingBuilding = self.game.getBuilding(targetX, targetY, self.z)
        if (buildingType is None):
            if (existingBuilding is None):
                return str(self.id) + " tried to build nothing"
            if (existingBuilding.type.builtBy != self.type):
                return str(self.id) + " can not continue construction on" \
                                    + " that type"
            existingBuilding.beBuilt()
        else:
            if (existingBuilding is not None):
                return str(self.id) + " tried to build on top of a building"
            if (buildingType.builtBy != self.type):
                return str(self.id) + " can not construct that type"
            if (self.owner.gold < buildingType.price):
                return "You do not have enough gold to build that"
            self.game.animations += [["build", self.id, targetX, targetY]]
            newBuilding = Building(self.game, targetX, targetY, self.z, \
                                   self.owner, buildingType)
            self.game.addObject(newBuilding)
            self.owner.gold -= buildingType.price
        self.actions -= 1
        self.changed = True
        return True


from gameObject import *

class UnitType(GameObject):
    def __init__(self, game):
        GameObject.__init__(self, game)
        self.name = "Unknown"
        self.price = 0
        self.hunger = 0
        self.trainTime = 0
        self.hp = 0
        self.armor = 0
        self.moves = 0
        self.actions = 0
        self.attackCost = 0
        self.damage = 0
        self.minRange = 0
        self.maxRange = 0
        self.trainedBy = ""
        self.canPaint = 0

    def toList(self):
        list = GameObject.toList(self)
        if (self.trainedBy is not None):
            trainerID = self.trainedBy.id
        else:
            trainerID = -1
        list.extend([self.name, self.price, self.hunger, self.trainTime,
                     self.hp, self.armor, self.moves, self.actions,
                     self.attackCost, self.damage, self.minRange,
                     self.maxRange, trainerID, self.canPaint])
        return list



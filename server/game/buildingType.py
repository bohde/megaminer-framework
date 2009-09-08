from gameObject import *

class BuildingType(GameObject):
    def __init__(self, game):
        GameObject.__init__(self, game)
        self.name = "Unknown"
        self.price = 0
        self.food = 0
        self.buildTime = 0
        self.hp = 0
        self.armor = 0
        self.builtBy = ""
        self.allowPaint = 0

    def toList(self):
        list = GameObject.toList(self)
        if (self.builtBy is not None):
            builderID = self.builtBy.id
        else:
            builderID = -1
        list.extend([self.name, self.price, self.food, self.buildTime,
                     self.hp, self.armor, builderID, self.allowPaint])
        return list


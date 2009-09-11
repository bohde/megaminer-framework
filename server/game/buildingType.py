from gameObject import *
import math

class BuildingType(GameObject):
    """
    Configurable members of BuildingType (see config/defaults.cfg)
    hpExp     - The exponential rate that hp increases per level
    armorExp  - The exponential rate that armor increases per level
    priceExp = 1.05  - The exponential rate that cost increases per level
    foodExp = 1.10  - The exponential rate that food production increases
    """

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

    def effArmor(self, level):
        """
        Returns this unit type's armor rating at the given level
        """
        armor = self.armor * self.armorExp ** level
        armor = int(math.floor(armor))
        return armor

    def effHP(self, level):
        """
        Returns this unit type's max hp at the given level
        """
        hp = self.hp * self.hpExp ** level
        hp = int(math.floor(hp))
        return hp


    def effPrice(self, level):
        price = self.price * self.priceExp ** level
        price = int(math.floor(price))
        return price



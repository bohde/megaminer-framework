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
        self.width = 1
        self.height = 1
        self.spawnX = 0
        self.spawnY = 0

    def toList(self):
        list = GameObject.toList(self)
        if (self.builtBy is not None):
            builderID = self.builtBy.id
        else:
            builderID = -1
        list.extend([self.name, self.price, self.food, self.buildTime,
                     self.hp, self.armor, builderID, self.allowPaint,
                     self.width, self.height, self.spawnX, self.spawnY])
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

    def adjArea(self, buildingX, buildingY):
        """
        Returns a set of tuples (x,y) that would be considered adjacent to
          a hypothetical building of this type at the given x,y
        """
        area = set([])
        for x in xrange(buildingX - 1, buildingX + self.width + 1):
            for y in xrange(buildingY, buildingY + self.height):
                area.add((x,y))
        for x in xrange(buildingX, buildingX + self.width):
            for y in xrange(buildingY - 1, buildingY + self.height + 1):
                area.add((x,y))
        return area

    def coveredArea(self, buildingX, buildingY):
        """
        Returns a set of tuples (x,y) that would be covered by
          a hypothetical building of this type at the given x,y
        """
        area = set([])
        for x in xrange(buildingX, buildingX + self.width):
            for y in xrange(buildingY, buildingY + self.height):
                area.add((x,y))
        return area


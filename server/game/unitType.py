from gameObject import *
import math

class UnitType(GameObject):
    """
    Configurable members of Unit (see config/defaults.cfg)
    hpExp     - The exponential rate that hp increases per level
    armorExp  - The exponential rate that armor increases per level
    priceExp - The exponential rate that cost increases per level
    damageExp - The exponential rate that damage increases per level
    paintBase - The min amount of gold gained by painting
    paintLinear - The amount of gold gained per difference in level
    """

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

    def effDamage(self, level):
        """
        returns this unit type's effective damage at the given level
        """
        dmg = self.damage * self.damageExp**level
        dmg = int(math.ceil(dmg))
        return dmg

    def artWorth(self, level, galleryLevel):
        lvlDiff = abs(level - galleryLevel)
        artWorth = self.paintBase + self.paintLinear * lvlDiff
        return artWorth


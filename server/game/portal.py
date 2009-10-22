from mappableObject import *
import math

class Portal(MappableObject):
    """
    Configurable members of Portal (see config/defaults.cfg)
    feeInit       - The initial portal fee value
    feeIncr       - The amount the fee is incremented for each unit
    feeMultiplier - The value multiplied to the portal fee each turn
    """

    def __init__(self, game, x, y, z, direction):
        """
        Direction is -1 if this portal links to the past, 1 if it links to
          the future.
        
        """
        MappableObject.__init__(self, game, x, y, z)
        self.direction = direction
        self.fee = Portal.feeInit

    def toList(self):
        list = MappableObject.toList(self)
        list.extend([self.direction, self.fee])
        return list

    def nextTurn(self):
        MappableObject.nextTurn(self)
        oldFee = int(self.fee)
        self.fee = int(math.floor(self.fee * Portal.feeMultiplier))
        if (oldFee != self.fee):
            self.changed = True

    def chargeToll(self, player):
        if (player.gold[self.z] < self.fee):
            return "You can not afford the portal fee"
        player.gold[self.z] -= self.fee
        self.fee += Portal.feeIncr
        self.changed = True
        return True


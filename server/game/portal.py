from mappableObject import *
import math

class Portal(MappableObject):
    feeInit = 25 #The initial portal fee value
    feeIncr = 10 #The amount the fee is incremented for each unit
    feeMultiplier = .8 #The value multiplied to the portal fee each turn

    def __init__(self, game, x, y, z, direction):
        """
        Direction is -1 if this portal links to the past, 1 if it links to
          the future.
        
        """
        MappableObject.__init__(self, game, x, y, z)
        self.direction = direction
        self.fee = Portal.feeInit

    def toList(self):
        list = GameObject.toList(self)
        list.extend([self.direction, self.fee])
        return list

    def nextTurn(self):
        MappableObject.nextTurn(self)
        oldFee = int(self.fee)
        self.fee = math.floor(self.fee * Portal.feeMultiplier)

    def chargeToll(self, player):
        if (player.gold[self.z] < self.fee):
            return "You can not afford the portal fee"
        player.gold[self.z] -= self.fee
        self.fee += Portal.feeIncr
        return True


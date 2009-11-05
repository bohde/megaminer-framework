# -*- python -*-

from library import library

class BaseAI:
    """@brief A basic AI interface.

    This class implements most the code an AI would need to interface with the lower-level game code.
    AIs should extend this class to get a lot of builer-plate code out of the way
    The provided AI class does just that.
    """
    initialized = False
    iteration = 0
    buildings = []
    buildingTypes = []
    portals = []
    terrains = []
    units = []
    unitTypes = []

    def startTurn(self):
        from GameObject import Building
        from GameObject import BuildingType
        from GameObject import Portal
        from GameObject import Terrain
        from GameObject import Unit
        from GameObject import UnitType

        BaseAI.buildings = [Building(library.getBuilding(i)) for i in xrange(library.getBuildingCount())]
        BaseAI.buildingTypes = [BuildingType(library.getBuildingType(i)) for i in xrange(library.getBuildingTypeCount())]
        BaseAI.portals = [Portal(library.getPortal(i)) for i in xrange(library.getPortalCount())]
        BaseAI.terrains = [Terrain(library.getTerrain(i)) for i in xrange(library.getTerrainCount())]
        BaseAI.units = [Unit(library.getUnit(i)) for i in xrange(library.getUnitCount())]
        BaseAI.unitTypes = [UnitType(library.getUnitType(i)) for i in xrange(library.getUnitTypeCount())]

        if not self.initialized:
            self.initialized = True
            self.init()
        BaseAI.iteration += 1;
        return self.run()
    
    @staticmethod
    def maxX():
        return library.getMaxX()

    @staticmethod
    def maxY():
        return library.getMaxY()

    @staticmethod
    def player0Gold0():
        """Player 0's past gold
        """
        return library.getPlayer0Gold0()

    @staticmethod
    def player0Gold1():
        """Player 0's present gold
        """
        return library.getPlayer0Gold1()

    @staticmethod
    def player0Gold2():
        """Player 0's future gold
        """
        return library.getPlayer0Gold2()

    @staticmethod
    def player1Gold0():
        """Player 1's past gold
        """
        return library.getPlayer1Gold0()

    @staticmethod
    def player1Gold1():
        """Player 1's present gold
        """
        return library.getPlayer1Gold1()

    @staticmethod
    def player1Gold2():
        """Player 1's future gold
        """
        return library.getPlayer1Gold2()

    @staticmethod
    def playerID():
        """Player Number; either 0 or 2
        """
        return library.getPlayerID()

    @staticmethod
    def turnNumber():
        return library.getTurnNumber()


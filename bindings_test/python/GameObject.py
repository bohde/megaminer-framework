# -*- python -*-

from library import library

from ExistentialError import ExistentialError

class GameObject(object):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self.ptr = ptr
    self.iteration = BaseAI.iteration


class Building(GameObject):
  """A building to shelter, feed, and/or create units.
  """
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self.ptr = ptr
    self.iteration = BaseAI.iteration
    
    self.ID = library.buildingGetObjectID(ptr)
  
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self.iteration == BaseAI.iteration:
      return True
    for i in BaseAI.buildings:
      if i.ID == self.ID:
        self.ptr = i.ptr
        self.iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  def train(self, unit):
    self.validify()
    if unit.__class__ not in [UnitType]:
      raise TypeError('unit should be of [UnitType]')
    unit.validify()
    return library.buildingTrain(self.ptr, unit.ptr)

  def cancel(self):
    self.validify()
    return library.buildingCancel(self.ptr)

  def getObjectID(self):
    self.validify()
    return library.buildingGetObjectID(self.ptr)

  def getX(self):
    self.validify()
    return library.buildingGetX(self.ptr)

  def getY(self):
    self.validify()
    return library.buildingGetY(self.ptr)

  def getZ(self):
    self.validify()
    return library.buildingGetZ(self.ptr)

  def getHp(self):
    self.validify()
    return library.buildingGetHp(self.ptr)

  def getLevel(self):
    self.validify()
    return library.buildingGetLevel(self.ptr)

  def getBuildingTypeID(self):
    self.validify()
    return library.buildingGetBuildingTypeID(self.ptr)

  def getOwnerID(self):
    self.validify()
    return library.buildingGetOwnerID(self.ptr)

  def getInTraining(self):
    self.validify()
    return library.buildingGetInTraining(self.ptr)

  def getProgress(self):
    self.validify()
    return library.buildingGetProgress(self.ptr)

  def getLinked(self):
    self.validify()
    return library.buildingGetLinked(self.ptr)

  def getComplete(self):
    self.validify()
    return library.buildingGetComplete(self.ptr)


class BuildingType(GameObject):
  """This defines the attributes of a kind of building.
  """
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self.ptr = ptr
    self.iteration = BaseAI.iteration
    
    self.ID = library.buildingTypeGetObjectID(ptr)
  
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self.iteration == BaseAI.iteration:
      return True
    for i in BaseAI.buildingTypes:
      if i.ID == self.ID:
        self.ptr = i.ptr
        self.iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  def getObjectID(self):
    self.validify()
    return library.buildingTypeGetObjectID(self.ptr)

  def getName(self):
    self.validify()
    return library.buildingTypeGetName(self.ptr)

  def getPrice(self):
    self.validify()
    return library.buildingTypeGetPrice(self.ptr)

  def getFood(self):
    self.validify()
    return library.buildingTypeGetFood(self.ptr)

  def getPastBuildTime(self):
    self.validify()
    return library.buildingTypeGetPastBuildTime(self.ptr)

  def getPresentBuildTime(self):
    self.validify()
    return library.buildingTypeGetPresentBuildTime(self.ptr)

  def getFutureBuildTime(self):
    self.validify()
    return library.buildingTypeGetFutureBuildTime(self.ptr)

  def getHp(self):
    self.validify()
    return library.buildingTypeGetHp(self.ptr)

  def getArmor(self):
    self.validify()
    return library.buildingTypeGetArmor(self.ptr)

  def getBuilderID(self):
    self.validify()
    return library.buildingTypeGetBuilderID(self.ptr)

  def getAllowPaint(self):
    self.validify()
    return library.buildingTypeGetAllowPaint(self.ptr)

  def getWidth(self):
    self.validify()
    return library.buildingTypeGetWidth(self.ptr)

  def getHeight(self):
    self.validify()
    return library.buildingTypeGetHeight(self.ptr)

  def getSpawnX(self):
    self.validify()
    return library.buildingTypeGetSpawnX(self.ptr)

  def getSpawnY(self):
    self.validify()
    return library.buildingTypeGetSpawnY(self.ptr)

  def getArmorExp(self):
    self.validify()
    return library.buildingTypeGetArmorExp(self.ptr)

  def getHpExp(self):
    self.validify()
    return library.buildingTypeGetHpExp(self.ptr)

  def getPriceExp(self):
    self.validify()
    return library.buildingTypeGetPriceExp(self.ptr)

  def getFoodExp(self):
    self.validify()
    return library.buildingTypeGetFoodExp(self.ptr)


class Portal(GameObject):
  """A connection between two adjacent times.
  """
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self.ptr = ptr
    self.iteration = BaseAI.iteration
    
    self.ID = library.portalGetObjectID(ptr)
  
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self.iteration == BaseAI.iteration:
      return True
    for i in BaseAI.portals:
      if i.ID == self.ID:
        self.ptr = i.ptr
        self.iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  def getObjectID(self):
    self.validify()
    return library.portalGetObjectID(self.ptr)

  def getX(self):
    self.validify()
    return library.portalGetX(self.ptr)

  def getY(self):
    self.validify()
    return library.portalGetY(self.ptr)

  def getZ(self):
    self.validify()
    return library.portalGetZ(self.ptr)

  def getDirection(self):
    self.validify()
    return library.portalGetDirection(self.ptr)

  def getFee(self):
    self.validify()
    return library.portalGetFee(self.ptr)

  def getFeeIncr(self):
    self.validify()
    return library.portalGetFeeIncr(self.ptr)

  def getFeeMultiplier(self):
    self.validify()
    return library.portalGetFeeMultiplier(self.ptr)


class Terrain(GameObject):
  """The attributes of a specific tile of the world.
  """
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self.ptr = ptr
    self.iteration = BaseAI.iteration
    
    self.ID = library.terrainGetObjectID(ptr)
  
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self.iteration == BaseAI.iteration:
      return True
    for i in BaseAI.terrains:
      if i.ID == self.ID:
        self.ptr = i.ptr
        self.iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  def getObjectID(self):
    self.validify()
    return library.terrainGetObjectID(self.ptr)

  def getX(self):
    self.validify()
    return library.terrainGetX(self.ptr)

  def getY(self):
    self.validify()
    return library.terrainGetY(self.ptr)

  def getZ(self):
    self.validify()
    return library.terrainGetZ(self.ptr)

  def getBlocksMove(self):
    self.validify()
    return library.terrainGetBlocksMove(self.ptr)

  def getBlocksBuild(self):
    self.validify()
    return library.terrainGetBlocksBuild(self.ptr)


class Unit(GameObject):
  """An entitiy that can move around the game and act.
  """
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self.ptr = ptr
    self.iteration = BaseAI.iteration
    
    self.ID = library.unitGetObjectID(ptr)
  
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self.iteration == BaseAI.iteration:
      return True
    for i in BaseAI.units:
      if i.ID == self.ID:
        self.ptr = i.ptr
        self.iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  def attack(self, x, y):
    self.validify()
    return library.unitAttack(self.ptr, x, y)

  def build(self, x, y, type):
    self.validify()
    if type.__class__ not in [BuildingType]:
      raise TypeError('type should be of [BuildingType]')
    type.validify()
    return library.unitBuild(self.ptr, x, y, type.ptr)

  def paint(self, x, y):
    self.validify()
    return library.unitPaint(self.ptr, x, y)

  def move(self, x, y):
    self.validify()
    return library.unitMove(self.ptr, x, y)

  def warp(self):
    self.validify()
    return library.unitWarp(self.ptr)

  def getObjectID(self):
    self.validify()
    return library.unitGetObjectID(self.ptr)

  def getX(self):
    self.validify()
    return library.unitGetX(self.ptr)

  def getY(self):
    self.validify()
    return library.unitGetY(self.ptr)

  def getZ(self):
    self.validify()
    return library.unitGetZ(self.ptr)

  def getHp(self):
    self.validify()
    return library.unitGetHp(self.ptr)

  def getLevel(self):
    self.validify()
    return library.unitGetLevel(self.ptr)

  def getUnitTypeID(self):
    self.validify()
    return library.unitGetUnitTypeID(self.ptr)

  def getOwnerID(self):
    self.validify()
    return library.unitGetOwnerID(self.ptr)

  def getActions(self):
    self.validify()
    return library.unitGetActions(self.ptr)

  def getMoves(self):
    self.validify()
    return library.unitGetMoves(self.ptr)


class UnitType(GameObject):
  """This defines the attributes of a kind of unit.
  """
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self.ptr = ptr
    self.iteration = BaseAI.iteration
    
    self.ID = library.unitTypeGetObjectID(ptr)
  
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self.iteration == BaseAI.iteration:
      return True
    for i in BaseAI.unitTypes:
      if i.ID == self.ID:
        self.ptr = i.ptr
        self.iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  def getObjectID(self):
    self.validify()
    return library.unitTypeGetObjectID(self.ptr)

  def getName(self):
    self.validify()
    return library.unitTypeGetName(self.ptr)

  def getPrice(self):
    self.validify()
    return library.unitTypeGetPrice(self.ptr)

  def getHunger(self):
    self.validify()
    return library.unitTypeGetHunger(self.ptr)

  def getTrainTime(self):
    self.validify()
    return library.unitTypeGetTrainTime(self.ptr)

  def getHp(self):
    self.validify()
    return library.unitTypeGetHp(self.ptr)

  def getArmor(self):
    self.validify()
    return library.unitTypeGetArmor(self.ptr)

  def getMoves(self):
    self.validify()
    return library.unitTypeGetMoves(self.ptr)

  def getActions(self):
    self.validify()
    return library.unitTypeGetActions(self.ptr)

  def getAttackCost(self):
    self.validify()
    return library.unitTypeGetAttackCost(self.ptr)

  def getDamage(self):
    self.validify()
    return library.unitTypeGetDamage(self.ptr)

  def getMinRange(self):
    self.validify()
    return library.unitTypeGetMinRange(self.ptr)

  def getMaxRange(self):
    self.validify()
    return library.unitTypeGetMaxRange(self.ptr)

  def getTrainerID(self):
    self.validify()
    return library.unitTypeGetTrainerID(self.ptr)

  def getCanPaint(self):
    self.validify()
    return library.unitTypeGetCanPaint(self.ptr)

  def getArmorExp(self):
    self.validify()
    return library.unitTypeGetArmorExp(self.ptr)

  def getHpExp(self):
    self.validify()
    return library.unitTypeGetHpExp(self.ptr)

  def getPriceExp(self):
    self.validify()
    return library.unitTypeGetPriceExp(self.ptr)

  def getDamageExp(self):
    self.validify()
    return library.unitTypeGetDamageExp(self.ptr)

  def getPaintBase(self):
    self.validify()
    return library.unitTypeGetPaintBase(self.ptr)

  def getPaintLinear(self):
    self.validify()
    return library.unitTypeGetPaintLinear(self.ptr)


//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that

#include "BaseAI.h"
#include "game.h"

int BaseAI::maxX()
{
  return getMaxX();
}
int BaseAI::maxY()
{
  return getMaxY();
}
int BaseAI::player0Gold0()
{
  return getPlayer0Gold0();
}
int BaseAI::player0Gold1()
{
  return getPlayer0Gold1();
}
int BaseAI::player0Gold2()
{
  return getPlayer0Gold2();
}
int BaseAI::player1Gold0()
{
  return getPlayer1Gold0();
}
int BaseAI::player1Gold1()
{
  return getPlayer1Gold1();
}
int BaseAI::player1Gold2()
{
  return getPlayer1Gold2();
}
int BaseAI::playerID()
{
  return getPlayerID();
}
int BaseAI::turnNumber()
{
  return getTurnNumber();
}

bool BaseAI::startTurn()
{
  static bool initialized = false;
  int count = 0;
  count = getBuildingCount();
  buildings.clear();
  buildings.resize(count);
  for(int i = 0; i < count; i++)
  {
    buildings[i] = Building(getBuilding(i));
  }
  count = getBuildingTypeCount();
  buildingTypes.clear();
  buildingTypes.resize(count);
  for(int i = 0; i < count; i++)
  {
    buildingTypes[i] = BuildingType(getBuildingType(i));
  }
  count = getPortalCount();
  portals.clear();
  portals.resize(count);
  for(int i = 0; i < count; i++)
  {
    portals[i] = Portal(getPortal(i));
  }
  count = getTerrainCount();
  terrains.clear();
  terrains.resize(count);
  for(int i = 0; i < count; i++)
  {
    terrains[i] = Terrain(getTerrain(i));
  }
  count = getUnitCount();
  units.clear();
  units.resize(count);
  for(int i = 0; i < count; i++)
  {
    units[i] = Unit(getUnit(i));
  }
  count = getUnitTypeCount();
  unitTypes.clear();
  unitTypes.resize(count);
  for(int i = 0; i < count; i++)
  {
    unitTypes[i] = UnitType(getUnitType(i));
  }
  if(!initialized)
  {
    initialized = true;
    init();
  }
  run();
}

//Convenience Functions
  UnitType BaseAI::getTypeFromUnit(Unit u)
  {
    return UnitType(::getTypeFromUnit(u.ptr));
  }
  BuildingType BaseAI::getTypeFromBuilding(Building b)
  {
    return BuildingType(::getTypeFromBuilding(b.ptr));
  }
  bool BaseAI::canMove(int x, int y, int z)
  {
    return ::canMove(x, y, z);
  }
  bool BaseAI::canBuild(int x, int y, int z)
  {
    return ::canBuild(x, y, z);
  }
  int BaseAI::effDamage(UnitType ut, int level)
  {
    return ::effDamage(ut.ptr, level);
  }
  int BaseAI::effFood(BuildingType bt, int level)
  {
    return ::effFood(bt.ptr, level);
  }
  int BaseAI::getGold(int playerNum, int z)
  {
    return ::getGold(playerNum, z);
  }
  int BaseAI::artWorth(int artistLevel, int galleryLevel)
  {
    return ::artWorth(artistLevel, galleryLevel);
  }
  int BaseAI::hunger(int playerID, int z)
  {
    return ::hunger(playerID, z);
  }
  int BaseAI::foodProduced(int playerID, int z)
  {
    return ::foodProduced(playerID, z);
  }
  int BaseAI::effBuildingPrice(BuildingType bt, int level)
  {
    return ::effBuildingPrice(bt.ptr, level);
  }
  int BaseAI::effUnitPrice(UnitType ut, int level)
  {
    return ::effUnitPrice(ut.ptr, level);
  }
  int BaseAI::effMaxHP(UnitType ut, int level)
  {
    return ::effMaxHP(ut.ptr, level);
  }
  int BaseAI::effBuildingArmor(BuildingType bt, int level)
  {
    return ::effBuildingArmor(bt.ptr, level);
  }
  int BaseAI::effUnitArmor(UnitType bt, int level)
  {
    return ::effUnitArmor(bt.ptr, level);
  }
  



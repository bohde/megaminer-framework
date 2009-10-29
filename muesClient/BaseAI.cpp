//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that

#include "BaseAI.h"
#include "game.h"

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
  run();
}

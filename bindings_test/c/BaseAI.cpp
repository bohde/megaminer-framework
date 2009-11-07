//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that

#include "BaseAI.h"
#include "game.h"

///////////////////////////////////////////////////////////////
/// Gets the X boundary for the map in all time periods.
///
/// For each time period, the map is a rectangle from (-max_x,-max_y)
/// to (max_x,max_y)
///////////////////////////////////////////////////////////////
int BaseAI::maxX()
{
  return getMaxX();
}

///////////////////////////////////////////////////////////////
/// Gets the Y boundary for the map in all time periods.
///
/// For each time period, the map is a rectangle from (-max_x,-max_y)
/// to (max_x,max_y)
///////////////////////////////////////////////////////////////
int BaseAI::maxY()
{
  return getMaxY();
}

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 0 has in the far past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
int BaseAI::player0Gold0()
{
  return getPlayer0Gold0();
}

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 0 has in the past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
int BaseAI::player0Gold1()
{
  return getPlayer0Gold1();
}

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 0 has in the present
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
int BaseAI::player0Gold2()
{
  return getPlayer0Gold2();
}

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 1 has in the far past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
int BaseAI::player1Gold0()
{
  return getPlayer1Gold0();
}

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 1 has in the past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
int BaseAI::player1Gold1()
{
  return getPlayer1Gold1();
}

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 1 has in the present
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
int BaseAI::player1Gold2()
{
  return getPlayer1Gold2();
}

///////////////////////////////////////////////////////////////
/// Returns the your player ID, either 0 or 1.
///
/// This value will match the ownerID of all your units.
///////////////////////////////////////////////////////////////
int BaseAI::playerID()
{
  return getPlayerID();
}

///////////////////////////////////////////////////////////////
/// Returns the current turn number
///
/// The first turn is turn 0.  Player 0 gets the first turn.
/// The second turn is turn 1.  Player 1 gets the first turn.
/// The game is ends at the end of turn 499 or earlier.
///////////////////////////////////////////////////////////////
int BaseAI::turnNumber()
{
  return getTurnNumber();
}

///////////////////////////////////////////////////////////////
/// Starts your turn.  You do not call this function.
///////////////////////////////////////////////////////////////
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

///////////////////////////////////////////////////////////////
/// Returns the type of the given unit.
///////////////////////////////////////////////////////////////
  UnitType BaseAI::getTypeFromUnit(Unit u)
  {
    return UnitType(::getTypeFromUnit(u.ptr));
  }

///////////////////////////////////////////////////////////////
/// Returns the type of the given building.
///////////////////////////////////////////////////////////////
  BuildingType BaseAI::getTypeFromBuilding(Building b)
  {
    return BuildingType(::getTypeFromBuilding(b.ptr));
  }

///////////////////////////////////////////////////////////////
/// Returns true if one of your units could move to the given coordinate
///
/// This function checks to see if this square contains any enemy units,
/// enemy buildings, or blocking terrain.
/// This is not an efficient implementation.  Feel free to write your own.
///////////////////////////////////////////////////////////////
  bool BaseAI::canMove(int x, int y, int z)
  {
    return ::canMove(x, y, z);
  }

///////////////////////////////////////////////////////////////
/// Returns true if this square is clear for you to build on.
///
/// This function checks to see if this square contains any enemy units,
/// buildings, or blocking terrain.
/// This is not an efficient implementation.  Feel free to write your own.
///////////////////////////////////////////////////////////////
  bool BaseAI::canBuild(int x, int y, int z)
  {
    return ::canBuild(x, y, z);
  }

///////////////////////////////////////////////////////////////
/// Returns the amount of raw damage a given type of unit would cause
/// at the given level.
///////////////////////////////////////////////////////////////
  int BaseAI::effDamage(UnitType ut, int level)
  {
    return ::effDamage(ut.ptr, level);
  }

///////////////////////////////////////////////////////////////
/// Returns the amount of food produced by a given type of building
/// at the given level.
///////////////////////////////////////////////////////////////
  int BaseAI::effFood(BuildingType bt, int level)
  {
    return ::effFood(bt.ptr, level);
  }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold the given player has in the given
/// time period
///////////////////////////////////////////////////////////////
  int BaseAI::getGold(int playerNum, int z)
  {
    return ::getGold(playerNum, z);
  }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold that would be gained if an artist
/// at the given level paints at a gallery of the given level.
///////////////////////////////////////////////////////////////
  int BaseAI::artWorth(int artistLevel, int galleryLevel)
  {
    return ::artWorth(artistLevel, galleryLevel);
  }

///////////////////////////////////////////////////////////////
/// Returns the sum of all hunger values for all units owned
/// by the given player in the given time period.
///////////////////////////////////////////////////////////////
  int BaseAI::hunger(int playerID, int z)
  {
    return ::hunger(playerID, z);
  }

///////////////////////////////////////////////////////////////
/// Returns the sum of all food produced by all buildings owned
/// by the given player in the given time period.
///////////////////////////////////////////////////////////////
  int BaseAI::foodProduced(int playerID, int z)
  {
    return ::foodProduced(playerID, z);
  }

///////////////////////////////////////////////////////////////
/// Returns the price of a building of the given type and level.
///////////////////////////////////////////////////////////////
  int BaseAI::effBuildingPrice(BuildingType bt, int level)
  {
    return ::effBuildingPrice(bt.ptr, level);
  }

///////////////////////////////////////////////////////////////
/// Returns the price of a unit of the given type and level.
///////////////////////////////////////////////////////////////
  int BaseAI::effUnitPrice(UnitType ut, int level)
  {
    return ::effUnitPrice(ut.ptr, level);
  }

///////////////////////////////////////////////////////////////
/// Returns the maxHP of a building of the given type and level.
///////////////////////////////////////////////////////////////
  int BaseAI::effBuildingMaxHP(BuildingType bt, int level)
  {
    return ::effBuildingMaxHP(bt.ptr, level);
  }

///////////////////////////////////////////////////////////////
/// Returns the maxHP of a building of the given type and level.
///////////////////////////////////////////////////////////////
  int BaseAI::effUnitMaxHP(UnitType ut, int level)
  {
    return ::effUnitMaxHP(ut.ptr, level);
  }

///////////////////////////////////////////////////////////////
/// Returns the armor of a building of the given type and level.
///////////////////////////////////////////////////////////////
  int BaseAI::effBuildingArmor(BuildingType bt, int level)
  {
    return ::effBuildingArmor(bt.ptr, level);
  }

///////////////////////////////////////////////////////////////
/// Returns the armor of a unit of the given type and level.
///////////////////////////////////////////////////////////////
  int BaseAI::effUnitArmor(UnitType ut, int level)
  {
    return ::effUnitArmor(ut.ptr, level);
  }
  



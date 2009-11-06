//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef BASEAI_H
#define BASEAI_H

#include <vector>
#include <ctime>
#include "game.h"
#include "wrappers.h"

/// \brief A basic AI interface.

///This class implements most the code an AI would need to interface with the lower-level game code.
///AIs should extend this class to get a lot of builer-plate code out of the way
///The provided AI class does just that.
class BaseAI
{
protected:
  std::vector<Building> buildings;
  std::vector<BuildingType> buildingTypes;
  std::vector<Portal> portals;
  std::vector<Terrain> terrains;
  std::vector<Unit> units;
  std::vector<UnitType> unitTypes;
public:
  int maxX();
  int maxY();
  ///Player 0's past gold
  int player0Gold0();
  ///Player 0's present gold
  int player0Gold1();
  ///Player 0's future gold
  int player0Gold2();
  ///Player 1's past gold
  int player1Gold0();
  ///Player 1's present gold
  int player1Gold1();
  ///Player 1's future gold
  int player1Gold2();
  ///Player Number; either 0 or 2
  int playerID();
  int turnNumber();
  
  ///
  ///Make this your username, which should be provided.
  virtual const char* username() = 0;
  ///
  ///Make this your password, which should be provided.
  virtual const char* password() = 0;
  ///
  ///This is run on turn 1 before run
  virtual void init() = 0;
  
  virtual bool run() = 0;

  bool startTurn();


  //Conveniencee Functions
  //The following functions are unnecessary, but handy.
  UnitType getTypeFromUnit(Unit u);
  BuildingType getTypeFromBuilding(Building b);
  bool canMove(int x, int y, int z);
  bool canBuild(int x, int y, int z);
  int effDamage(UnitType ut, int level);
  int effFood(BuildingType bt, int level);
  int getGold(int playerNum, int z);
  int artWorth(int artistLevel, int galleryLevel);
  int hunger(int playerID, int z);
  int foodProduced(int playerID, int z);
  int effBuildingPrice(BuildingType bt, int level);
  int effUnitPrice(UnitType ut, int level);
  int effMaxHP(UnitType ut, int level);
  int effBuildingArmor(BuildingType bt, int level);
  int effUnitArmor(UnitType bt, int level);


};

#endif

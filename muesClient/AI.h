#ifndef AI_H
#define AI_H

#include "BaseAI.h"
#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

///The class implementing gameplay logic.
class AI: public BaseAI
{
public:
  virtual const char* username();
  virtual const char* password();
  virtual void init();
  virtual bool run();

  void trainUnits(Building& b);
  void doArtist(Unit& u);
  void doEngineer(Unit& u);
  bool areaClear(int x, int y, int z, int typeIndex);
  bool isClear(int x, int y, int z);
  Building* getBuilding(int x, int y, int z);
  void doCombatUnit(Unit& u);
  Unit* anyInRange(Unit& u);

  void randomWalk(Unit& u, int moves);
  Portal* getPortalAt(int x, int y, int z);
  bool canWalk(int x, int y, int z);

  UnitType getType(Unit& u);
  BuildingType getType(Building& b);
  int distance(int x1, int y1, int z1, int x2, int y2, int z2);
  int distance(Unit& a, Unit& b);
  int distance(Unit& a, Portal& b);
  int distance(Unit& a, Building& b);

  int goldSpent[6];
  int portalFees[100];
  int getGold(int playerNum, int z);
  int effPrice(BuildingType bt, int level);
  int effPrice(UnitType ut, int level);
  void spendGold(int playerNum, int z, int gold);
  int getPortalIndex(Portal p);
  int getPortalFee(Portal p);

};



#endif

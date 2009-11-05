//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef GAME_H
#define GAME_H

#include "network.h"
#include "structures.h"

#ifdef WIN32
#define DLLEXPORT extern "C" __declspec(dllexport)
#else
#define DLLEXPORT
#endif

#ifdef __cplusplus
extern "C"
{
#endif
  DLLEXPORT bool serverLogin(int socket, const char* username, const char* password);
  DLLEXPORT int createGame();
  DLLEXPORT int joinGame(int id);

  DLLEXPORT void endTurn();
  DLLEXPORT void getStatus();


//commands

  DLLEXPORT bool buildingTrain(_Building* object, _UnitType* unit);
  DLLEXPORT bool buildingCancel(_Building* object);
  DLLEXPORT bool unitAttack(_Unit* object, int x, int y);
  DLLEXPORT bool unitBuild(_Unit* object, int x, int y, _BuildingType* type);
  DLLEXPORT bool unitPaint(_Unit* object, int x, int y);
  DLLEXPORT bool unitMove(_Unit* object, int x, int y);
  DLLEXPORT bool unitWarp(_Unit* object);

//accessors

DLLEXPORT int getMaxX();
DLLEXPORT int getMaxY();
DLLEXPORT int getPlayer0Gold0();
DLLEXPORT int getPlayer0Gold1();
DLLEXPORT int getPlayer0Gold2();
DLLEXPORT int getPlayer1Gold0();
DLLEXPORT int getPlayer1Gold1();
DLLEXPORT int getPlayer1Gold2();
DLLEXPORT int getPlayerID();
DLLEXPORT int getTurnNumber();

DLLEXPORT _Building* getBuilding(int num);
DLLEXPORT int getBuildingCount();

DLLEXPORT _BuildingType* getBuildingType(int num);
DLLEXPORT int getBuildingTypeCount();

DLLEXPORT _Portal* getPortal(int num);
DLLEXPORT int getPortalCount();

DLLEXPORT _Terrain* getTerrain(int num);
DLLEXPORT int getTerrainCount();

DLLEXPORT _Unit* getUnit(int num);
DLLEXPORT int getUnitCount();

DLLEXPORT _UnitType* getUnitType(int num);
DLLEXPORT int getUnitTypeCount();

//Convenience Functions
DLLEXPORT _UnitType* getTypeFromUnit(_Unit* u);
DLLEXPORT _BuildingType* getTypeFromBuilding(_Building* b);
DLLEXPORT bool canMove(int x, int y, int z);
DLLEXPORT bool canBuild(int x, int y, int z);
DLLEXPORT int effDamage(_UnitType* ut, int level);
DLLEXPORT int effFood(_BuildingType* bt, int level);
DLLEXPORT int getGold(int playerNum, int z);
DLLEXPORT int artWorth(int artistLevel, int galleryLevel);
DLLEXPORT int hunger(int playerID, int z);
DLLEXPORT int foodProduced(int playerID, int z);
DLLEXPORT int effBuildingPrice(_BuildingType* bt, int level);
DLLEXPORT int effUnitPrice(_BuildingType* ut, int level);
DLLEXPORT int effMaxHP(_UnitType* ut, int level);
DLLEXPORT int effArmor(_BuildingType* bt, int level);


  DLLEXPORT int networkLoop(int socket);
#ifdef __cplusplus
}
#endif

#endif

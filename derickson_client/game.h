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
  DLLEXPORT bool login(int socket, const char* username, const char* password);
  DLLEXPORT int createGame();
  DLLEXPORT int joinGame(int id);

  DLLEXPORT void endTurn();
  DLLEXPORT void getStatus();


//commands

  DLLEXPORT bool buildingTrain(int objectID, int unit);
  DLLEXPORT bool buildingCancel(int objectID);
  DLLEXPORT bool unitAttack(int objectID, int x, int y);
  DLLEXPORT bool unitBuild(int objectID, int x, int y, int type);
  DLLEXPORT bool unitPaint(int objectID, int x, int y);
  DLLEXPORT bool unitMove(int objectID, int x, int y);
  DLLEXPORT bool unitWarp(int objectID);

//accessors

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



  DLLEXPORT int networkLoop(int socket);
#ifdef __cplusplus
}
#endif

#endif

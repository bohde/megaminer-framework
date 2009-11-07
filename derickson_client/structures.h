//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef STRUCTURES_H
#define STRUCTURES_H

struct _Building
{
  int objectID;
  int x;
  int y;
  int z;
  int hp;
  int level;
  int buildingTypeID;
  int inTraining;
  int progress;
  int linked;
  int complete;
};
struct _BuildingType
{
  int objectID;
  char* name;
  int price;
  int food;
  int pastBuildTime;
  int presentBuildTime;
  int futureBuildTime;
  int hp;
  int armor;
  int builderID;
  int allowPaint;
  int width;
  int height;
  int spawnX;
  int spawnY;
};
struct _Portal
{
  int objectID;
  int x;
  int y;
  int z;
  int direction;
  int fee;
};
struct _Terrain
{
  int objectID;
  int x;
  int y;
  int z;
  int blockmove;
  int blockbuild;
};
struct _Unit
{
  int objectID;
  int x;
  int y;
  int z;
  int hp;
  int level;
  int unitTypeID;
  int ownerIndex;
  int actions;
  int moves;
};
struct _UnitType
{
  int objectID;
  char* name;
  int price;
  int hunger;
  int traintime;
  int hp;
  int armor;
  int moves;
  int actions;
  int attackcost;
  int damage;
  int minrange;
  int maxrange;
  int trainerID;
  int canpaint;
};

#endif

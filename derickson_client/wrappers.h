// -*-c++-*-

#ifndef WRAPPERS_H
#define WRAPPERS_H

#include <cstdlib>
#include "structures.h"

class Building;
class BuildingType;
class Portal;
class Terrain;
class Unit;
class UnitType;

class Building {
  _Building* ptr;
 public:
  Building(_Building* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int hp();
  int level();
  int buildingTypeID();
  int inTraining();
  int progress();
  int linked();
  int complete();

  // Actions
  bool train(int unit);
  bool cancel();
};

class BuildingType {
  _BuildingType* ptr;
 public:
  BuildingType(_BuildingType* ptr = NULL);

  // Accessors
  int objectID();
  char* name();
  int price();
  int food();
  int pastBuildTime();
  int presentBuildTime();
  int futureBuildTime();
  int hp();
  int armor();
  int builderID();
  int allowPaint();
  int width();
  int height();
  int spawnX();
  int spawnY();

  // Actions
};

class Portal {
  _Portal* ptr;
 public:
  Portal(_Portal* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int direction();
  int fee();

  // Actions
};

class Terrain {
  _Terrain* ptr;
 public:
  Terrain(_Terrain* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int blockmove();
  int blockbuild();

  // Actions
};

class Unit {
  _Unit* ptr;
 public:
  Unit(_Unit* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int hp();
  int level();
  int unitTypeID();
  int ownerIndex();
  int actions();
  int moves();

  // Actions
  bool attack(int x, int y);
  bool build(int x, int y, int type);
  bool paint(int x, int y);
  bool move(int x, int y);
  bool warp();
};

class UnitType {
  _UnitType* ptr;
 public:
  UnitType(_UnitType* ptr = NULL);

  // Accessors
  int objectID();
  char* name();
  int price();
  int hunger();
  int traintime();
  int hp();
  int armor();
  int moves();
  int actions();
  int attackcost();
  int damage();
  int minrange();
  int maxrange();
  int trainerID();
  int canpaint();

  // Actions
};


#endif

// -*-c++-*-

#ifndef WRAPPERS_H
#define WRAPPERS_H

#include <iostream>
#include <cstdlib>
#include "structures.h"

class Building;
class BuildingType;
class Portal;
class Terrain;
class Unit;
class UnitType;

///A building to shelter, feed, and/or create units.
class Building {
  public:
  _Building* ptr;
  Building(_Building* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int hp();
  int level();
  int buildingTypeID();
  int ownerID();
  int inTraining();
  int progress();
  int linked();
  int complete();

  // Actions
  bool train(UnitType& unit);
  bool cancel();

  friend std::ostream& operator<<(std::ostream& stream, Building ob);
};

///This defines the attributes of a kind of building.
class BuildingType {
  public:
  _BuildingType* ptr;
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
  float armorExp();
  float hpExp();
  float priceExp();
  float foodExp();

  // Actions

  friend std::ostream& operator<<(std::ostream& stream, BuildingType ob);
};

///A connection between two adjacent times.
class Portal {
  public:
  _Portal* ptr;
  Portal(_Portal* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int direction();
  int fee();
  int feeIncr();
  float feeMultiplier();

  // Actions

  friend std::ostream& operator<<(std::ostream& stream, Portal ob);
};

///The attributes of a specific tile of the world.
class Terrain {
  public:
  _Terrain* ptr;
  Terrain(_Terrain* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int blockmove();
  int blockbuild();

  // Actions

  friend std::ostream& operator<<(std::ostream& stream, Terrain ob);
};

///An entitiy that can move around the game and act.
class Unit {
  public:
  _Unit* ptr;
  Unit(_Unit* ptr = NULL);

  // Accessors
  int objectID();
  int x();
  int y();
  int z();
  int hp();
  int level();
  int unitTypeID();
  int ownerID();
  int actions();
  int moves();

  // Actions
  bool attack(int x, int y);
  bool build(int x, int y, BuildingType& type);
  bool paint(int x, int y);
  bool move(int x, int y);
  bool warp();

  friend std::ostream& operator<<(std::ostream& stream, Unit ob);
};

///This defines the attributes of a kind of unit.
class UnitType {
  public:
  _UnitType* ptr;
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
  float armorExp();
  float hpExp();
  float priceExp();
  float damageExp();
  int paintBase();
  int paintLinear();

  // Actions

  friend std::ostream& operator<<(std::ostream& stream, UnitType ob);
};


#endif

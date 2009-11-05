// -*-c++-*-

#include "wrappers.h"
#include "game.h"

Building::Building(_Building* ptr) : ptr(ptr)
{

}

int Building::objectID()
{
  return ptr->objectID;
}

int Building::x()
{
  return ptr->x;
}

int Building::y()
{
  return ptr->y;
}

int Building::z()
{
  return ptr->z;
}

int Building::hp()
{
  return ptr->hp;
}

int Building::level()
{
  return ptr->level;
}

int Building::buildingTypeID()
{
  return ptr->buildingTypeID;
}

int Building::inTraining()
{
  return ptr->inTraining;
}

int Building::progress()
{
  return ptr->progress;
}

int Building::linked()
{
  return ptr->linked;
}

int Building::complete()
{
  return ptr->complete;
}


bool Building::train(int unit)
{
  return buildingTrain(ptr->objectID, unit);
}

bool Building::cancel()
{
  return buildingCancel(ptr->objectID);
}


BuildingType::BuildingType(_BuildingType* ptr) : ptr(ptr)
{

}

int BuildingType::objectID()
{
  return ptr->objectID;
}

char* BuildingType::name()
{
  return ptr->name;
}

int BuildingType::price()
{
  return ptr->price;
}

int BuildingType::food()
{
  return ptr->food;
}

int BuildingType::pastBuildTime()
{
  return ptr->pastBuildTime;
}

int BuildingType::presentBuildTime()
{
  return ptr->presentBuildTime;
}

int BuildingType::futureBuildTime()
{
  return ptr->futureBuildTime;
}

int BuildingType::hp()
{
  return ptr->hp;
}

int BuildingType::armor()
{
  return ptr->armor;
}

int BuildingType::builderID()
{
  return ptr->builderID;
}

int BuildingType::allowPaint()
{
  return ptr->allowPaint;
}

int BuildingType::width()
{
  return ptr->width;
}

int BuildingType::height()
{
  return ptr->height;
}

int BuildingType::spawnX()
{
  return ptr->spawnX;
}

int BuildingType::spawnY()
{
  return ptr->spawnY;
}



Portal::Portal(_Portal* ptr) : ptr(ptr)
{

}

int Portal::objectID()
{
  return ptr->objectID;
}

int Portal::x()
{
  return ptr->x;
}

int Portal::y()
{
  return ptr->y;
}

int Portal::z()
{
  return ptr->z;
}

int Portal::direction()
{
  return ptr->direction;
}

int Portal::fee()
{
  return ptr->fee;
}



Terrain::Terrain(_Terrain* ptr) : ptr(ptr)
{

}

int Terrain::objectID()
{
  return ptr->objectID;
}

int Terrain::x()
{
  return ptr->x;
}

int Terrain::y()
{
  return ptr->y;
}

int Terrain::z()
{
  return ptr->z;
}

int Terrain::blockmove()
{
  return ptr->blockmove;
}

int Terrain::blockbuild()
{
  return ptr->blockbuild;
}



Unit::Unit(_Unit* ptr) : ptr(ptr)
{

}

int Unit::objectID()
{
  return ptr->objectID;
}

int Unit::x()
{
  return ptr->x;
}

int Unit::y()
{
  return ptr->y;
}

int Unit::z()
{
  return ptr->z;
}

int Unit::hp()
{
  return ptr->hp;
}

int Unit::level()
{
  return ptr->level;
}

int Unit::unitTypeID()
{
  return ptr->unitTypeID;
}

int Unit::ownerIndex()
{
  return ptr->ownerIndex;
}

int Unit::actions()
{
  return ptr->actions;
}

int Unit::moves()
{
  return ptr->moves;
}


bool Unit::attack(int x, int y)
{
  return unitAttack(ptr->objectID, x, y);
}

bool Unit::build(int x, int y, int type)
{
  return unitBuild(ptr->objectID, x, y, type);
}

bool Unit::paint(int x, int y)
{
  return unitPaint(ptr->objectID, x, y);
}

bool Unit::move(int x, int y)
{
  return unitMove(ptr->objectID, x, y);
}

bool Unit::warp()
{
  return unitWarp(ptr->objectID);
}


UnitType::UnitType(_UnitType* ptr) : ptr(ptr)
{

}

int UnitType::objectID()
{
  return ptr->objectID;
}

char* UnitType::name()
{
  return ptr->name;
}

int UnitType::price()
{
  return ptr->price;
}

int UnitType::hunger()
{
  return ptr->hunger;
}

int UnitType::traintime()
{
  return ptr->traintime;
}

int UnitType::hp()
{
  return ptr->hp;
}

int UnitType::armor()
{
  return ptr->armor;
}

int UnitType::moves()
{
  return ptr->moves;
}

int UnitType::actions()
{
  return ptr->actions;
}

int UnitType::attackcost()
{
  return ptr->attackcost;
}

int UnitType::damage()
{
  return ptr->damage;
}

int UnitType::minrange()
{
  return ptr->minrange;
}

int UnitType::maxrange()
{
  return ptr->maxrange;
}

int UnitType::trainerID()
{
  return ptr->trainerID;
}

int UnitType::canpaint()
{
  return ptr->canpaint;
}




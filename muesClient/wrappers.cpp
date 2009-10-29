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

int Building::ownerID()
{
  return ptr->ownerID;
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


bool Building::train(UnitType& unit)
{
  return buildingTrain(ptr, unit.ptr);
}

bool Building::cancel()
{
  return buildingCancel(ptr);
}


std::ostream& operator<<(std::ostream& stream,Building ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "x: " << ob.ptr->x  <<'\n';
  stream << "y: " << ob.ptr->y  <<'\n';
  stream << "z: " << ob.ptr->z  <<'\n';
  stream << "hp: " << ob.ptr->hp  <<'\n';
  stream << "level: " << ob.ptr->level  <<'\n';
  stream << "buildingTypeID: " << ob.ptr->buildingTypeID  <<'\n';
  stream << "ownerID: " << ob.ptr->ownerID  <<'\n';
  stream << "inTraining: " << ob.ptr->inTraining  <<'\n';
  stream << "progress: " << ob.ptr->progress  <<'\n';
  stream << "linked: " << ob.ptr->linked  <<'\n';
  stream << "complete: " << ob.ptr->complete  <<'\n';
  return stream;
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

float BuildingType::armorExp()
{
  return ptr->armorExp;
}

float BuildingType::hpExp()
{
  return ptr->hpExp;
}

float BuildingType::priceExp()
{
  return ptr->priceExp;
}

float BuildingType::foodExp()
{
  return ptr->foodExp;
}



std::ostream& operator<<(std::ostream& stream,BuildingType ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "name: " << ob.ptr->name  <<'\n';
  stream << "price: " << ob.ptr->price  <<'\n';
  stream << "food: " << ob.ptr->food  <<'\n';
  stream << "pastBuildTime: " << ob.ptr->pastBuildTime  <<'\n';
  stream << "presentBuildTime: " << ob.ptr->presentBuildTime  <<'\n';
  stream << "futureBuildTime: " << ob.ptr->futureBuildTime  <<'\n';
  stream << "hp: " << ob.ptr->hp  <<'\n';
  stream << "armor: " << ob.ptr->armor  <<'\n';
  stream << "builderID: " << ob.ptr->builderID  <<'\n';
  stream << "allowPaint: " << ob.ptr->allowPaint  <<'\n';
  stream << "width: " << ob.ptr->width  <<'\n';
  stream << "height: " << ob.ptr->height  <<'\n';
  stream << "spawnX: " << ob.ptr->spawnX  <<'\n';
  stream << "spawnY: " << ob.ptr->spawnY  <<'\n';
  stream << "armorExp: " << ob.ptr->armorExp  <<'\n';
  stream << "hpExp: " << ob.ptr->hpExp  <<'\n';
  stream << "priceExp: " << ob.ptr->priceExp  <<'\n';
  stream << "foodExp: " << ob.ptr->foodExp  <<'\n';
  return stream;
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



std::ostream& operator<<(std::ostream& stream,Portal ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "x: " << ob.ptr->x  <<'\n';
  stream << "y: " << ob.ptr->y  <<'\n';
  stream << "z: " << ob.ptr->z  <<'\n';
  stream << "direction: " << ob.ptr->direction  <<'\n';
  stream << "fee: " << ob.ptr->fee  <<'\n';
  return stream;
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



std::ostream& operator<<(std::ostream& stream,Terrain ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "x: " << ob.ptr->x  <<'\n';
  stream << "y: " << ob.ptr->y  <<'\n';
  stream << "z: " << ob.ptr->z  <<'\n';
  stream << "blockmove: " << ob.ptr->blockmove  <<'\n';
  stream << "blockbuild: " << ob.ptr->blockbuild  <<'\n';
  return stream;
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

int Unit::ownerID()
{
  return ptr->ownerID;
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
  return unitAttack(ptr, x, y);
}

bool Unit::build(int x, int y, BuildingType& type)
{
  return unitBuild(ptr, x, y, type.ptr);
}

bool Unit::paint(int x, int y)
{
  return unitPaint(ptr, x, y);
}

bool Unit::move(int x, int y)
{
  return unitMove(ptr, x, y);
}

bool Unit::warp()
{
  return unitWarp(ptr);
}


std::ostream& operator<<(std::ostream& stream,Unit ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "x: " << ob.ptr->x  <<'\n';
  stream << "y: " << ob.ptr->y  <<'\n';
  stream << "z: " << ob.ptr->z  <<'\n';
  stream << "hp: " << ob.ptr->hp  <<'\n';
  stream << "level: " << ob.ptr->level  <<'\n';
  stream << "unitTypeID: " << ob.ptr->unitTypeID  <<'\n';
  stream << "ownerID: " << ob.ptr->ownerID  <<'\n';
  stream << "actions: " << ob.ptr->actions  <<'\n';
  stream << "moves: " << ob.ptr->moves  <<'\n';
  return stream;
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

float UnitType::armorExp()
{
  return ptr->armorExp;
}

float UnitType::hpExp()
{
  return ptr->hpExp;
}

float UnitType::priceExp()
{
  return ptr->priceExp;
}

float UnitType::damageExp()
{
  return ptr->damageExp;
}

int UnitType::paintBase()
{
  return ptr->paintBase;
}

int UnitType::paintLinear()
{
  return ptr->paintLinear;
}



std::ostream& operator<<(std::ostream& stream,UnitType ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "name: " << ob.ptr->name  <<'\n';
  stream << "price: " << ob.ptr->price  <<'\n';
  stream << "hunger: " << ob.ptr->hunger  <<'\n';
  stream << "traintime: " << ob.ptr->traintime  <<'\n';
  stream << "hp: " << ob.ptr->hp  <<'\n';
  stream << "armor: " << ob.ptr->armor  <<'\n';
  stream << "moves: " << ob.ptr->moves  <<'\n';
  stream << "actions: " << ob.ptr->actions  <<'\n';
  stream << "attackcost: " << ob.ptr->attackcost  <<'\n';
  stream << "damage: " << ob.ptr->damage  <<'\n';
  stream << "minrange: " << ob.ptr->minrange  <<'\n';
  stream << "maxrange: " << ob.ptr->maxrange  <<'\n';
  stream << "trainerID: " << ob.ptr->trainerID  <<'\n';
  stream << "canpaint: " << ob.ptr->canpaint  <<'\n';
  stream << "armorExp: " << ob.ptr->armorExp  <<'\n';
  stream << "hpExp: " << ob.ptr->hpExp  <<'\n';
  stream << "priceExp: " << ob.ptr->priceExp  <<'\n';
  stream << "damageExp: " << ob.ptr->damageExp  <<'\n';
  stream << "paintBase: " << ob.ptr->paintBase  <<'\n';
  stream << "paintLinear: " << ob.ptr->paintLinear  <<'\n';
  return stream;
}


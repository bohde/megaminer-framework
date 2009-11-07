// -*-c++-*-

#include "wrappers.h"
#include "game.h"

Building::Building(_Building* ptr) : ptr(ptr)
{

}

///////////////////////////////////////////////////////////////////
/// Returns a unique identifier for this object.  This ID will only
/// be assigned to this object, and will never change.
///////////////////////////////////////////////////////////////////
int Building::objectID()
{
  return ptr->objectID;
}

///////////////////////////////////////////////////////////////////
/// Returns the x coordinate of this object.  For buildings, this
/// is the position of the corner closest to (-inf, -inf).
///////////////////////////////////////////////////////////////////
int Building::x()
{
  return ptr->x;
}

///////////////////////////////////////////////////////////////////
/// Returns the y coordinate of this object.  For buildings, this
/// is the position of the corner closest to (-inf, -inf).
///////////////////////////////////////////////////////////////////
int Building::y()
{
  return ptr->y;
}

///////////////////////////////////////////////////////////////////
/// Returns the z coordinate of this object.  0 is the far past,
/// 1 is the past, 0 is the present.
///////////////////////////////////////////////////////////////////
int Building::z()
{
  return ptr->z;
}

///////////////////////////////////////////////////////////////////
/// Returns the current hp of this building.
///////////////////////////////////////////////////////////////////
int Building::hp()
{
  return ptr->hp;
}

///////////////////////////////////////////////////////////////////
/// Returns the level of this building.
///////////////////////////////////////////////////////////////////
int Building::level()
{
  return ptr->level;
}

///////////////////////////////////////////////////////////////////
/// Returns the object ID of this building's associated type.
///////////////////////////////////////////////////////////////////
int Building::buildingTypeID()
{
  return ptr->buildingTypeID;
}

///////////////////////////////////////////////////////////////////
/// Returns the id of the player controlling this building.
/// Either 0 or 1.
///////////////////////////////////////////////////////////////////
int Building::ownerID()
{
  return ptr->ownerID;
}

///////////////////////////////////////////////////////////////////
/// The objectID of the unit type that is being trained, or -1 if
/// no unit is being trained.
///////////////////////////////////////////////////////////////////
int Building::inTraining()
{
  return ptr->inTraining;
}

///////////////////////////////////////////////////////////////////
/// Returns the number of turns this building has been training
/// a unit.
///////////////////////////////////////////////////////////////////
int Building::progress()
{
  return ptr->progress;
}

///////////////////////////////////////////////////////////////////
/// Returns 1 if this building has a cascaded version of itself in
/// the next time period, 0 otherwise.
///////////////////////////////////////////////////////////////////
int Building::linked()
{
  return ptr->linked;
}

///////////////////////////////////////////////////////////////////
/// Returns 1 if this building has been completed, 0 otherwise.
///////////////////////////////////////////////////////////////////
int Building::complete()
{
  return ptr->complete;
}

///////////////////////////////////////////////////////////////////
/// Begins training the given unit type.
///////////////////////////////////////////////////////////////////
bool Building::train(UnitType& unit)
{
  return buildingTrain(ptr, unit.ptr);
}

///////////////////////////////////////////////////////////////////
/// If this building has not been completed, cancels construction
/// of this building.  The building is destroyed for a full refund.
/// If this building is completed and is training a unit, cancels
/// the training for a full refund.
///////////////////////////////////////////////////////////////////
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

//////////////////////////////////////////////////////////////
/// Returns the object id of the unit type that can build this
/// building type.
//////////////////////////////////////////////////////////////
int BuildingType::builderID()
{
  return ptr->builderID;
}

/////////////////////////////////////////////////////////////
/// Returns 1 if this building type allows units to paint,
/// 0 otherwise.
////////////////////////////////////////////////////////////
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

/////////////////////////////////////////////////////////////
/// Returns the x offest of newly created units from this building.
///
/// Newly trained units appear at (x+spawnX, y+spawnY
////////////////////////////////////////////////////////////
int BuildingType::spawnX()
{
  return ptr->spawnX;
}

/////////////////////////////////////////////////////////////
/// Returns the y offest of newly created units from this building.
///
/// Newly trained units appear at (x+spawnX, y+spawnY
////////////////////////////////////////////////////////////
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

///////////////////////////////////////////////////////////////
/// Returns 1 if this portal leads forward in time, -1 otherwise
///
/// When a unit performs a warp action, this value is added to the 
/// unit's z coordinate.
///////////////////////////////////////////////////////////////
int Portal::direction()
{
  return ptr->direction;
}

//////////////////////////////////////////////////////////////////
/// Returns the price in gold that you will pay if a unit warps through
/// this portal.
/////////////////////////////////////////////////////////////////
int Portal::fee()
{
  return ptr->fee;
}

/////////////////////////////////////////////////////////////////
/// Returns the amount the fee will increase every time a unit
/// uses this portal.
/////////////////////////////////////////////////////////////////
int Portal::feeIncr()
{
  return ptr->feeIncr;
}

///////////////////////////////////////////////////////////////////
/// Returns the value multiplied to the portal fee at the end of
/// each turn.
///////////////////////////////////////////////////////////////////
float Portal::feeMultiplier()
{
  return ptr->feeMultiplier;
}



std::ostream& operator<<(std::ostream& stream,Portal ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "x: " << ob.ptr->x  <<'\n';
  stream << "y: " << ob.ptr->y  <<'\n';
  stream << "z: " << ob.ptr->z  <<'\n';
  stream << "direction: " << ob.ptr->direction  <<'\n';
  stream << "fee: " << ob.ptr->fee  <<'\n';
  stream << "feeIncr: " << ob.ptr->feeIncr  <<'\n';
  stream << "feeMultiplier: " << ob.ptr->feeMultiplier  <<'\n';
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

//////////////////////////////////////////////////////////////////
/// Returns 1 if this object prevents units from moving onto this square,
/// 0 otherwise.
//////////////////////////////////////////////////////////////
int Terrain::blocksMove()
{
  return ptr->blocksMove;
}

/////////////////////////////////////////////////////////////////
/// Returns 1 if this object pervents buildings from being placed
/// on this square, 0 otherwise.
/////////////////////////////////////////////////////////////////
int Terrain::blocksBuild()
{
  return ptr->blocksBuild;
}



std::ostream& operator<<(std::ostream& stream,Terrain ob)
{
  stream << "objectID: " << ob.ptr->objectID  <<'\n';
  stream << "x: " << ob.ptr->x  <<'\n';
  stream << "y: " << ob.ptr->y  <<'\n';
  stream << "z: " << ob.ptr->z  <<'\n';
  stream << "blocksMove: " << ob.ptr->blocksMove  <<'\n';
  stream << "blocksBuild: " << ob.ptr->blocksBuild  <<'\n';
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

/////////////////////////////////////////////////////////////
/// The unit attempts to generate gold by painting.  The x,y 
/// coordinate must contain a Gallery amd must be adjacent or
/// under this unit.
/////////////////////////////////////////////////////////////
bool Unit::paint(int x, int y)
{
  return unitPaint(ptr, x, y);
}

bool Unit::move(int x, int y)
{
  return unitMove(ptr, x, y);
}

//////////////////////////////////////////////////////////////
/// Makes this unit attempt to use a portal.
///
/// The portal under this unit adds its direction member variable to 
/// this unit's z coordinate.  The portal's fee is paid and then increased.
////////////////////////////////////////////////////////////////
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

int UnitType::trainTime()
{
  return ptr->trainTime;
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

int UnitType::attackCost()
{
  return ptr->attackCost;
}

int UnitType::damage()
{
  return ptr->damage;
}

int UnitType::minRange()
{
  return ptr->minRange;
}

int UnitType::maxRange()
{
  return ptr->maxRange;
}

////////////////////////////////////////////////////////
/// Returns the objectID of the building that can train this unit.
////////////////////////////////////////////////////////
int UnitType::trainerID()
{
  return ptr->trainerID;
}

///////////////////////////////////////////////////////
/// Returns 1 if this unit can perform the paint action, 
/// 0 otherwise.
//////////////////////////////////////////////////////
int UnitType::canPaint()
{
  return ptr->canPaint;
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
  stream << "trainTime: " << ob.ptr->trainTime  <<'\n';
  stream << "hp: " << ob.ptr->hp  <<'\n';
  stream << "armor: " << ob.ptr->armor  <<'\n';
  stream << "moves: " << ob.ptr->moves  <<'\n';
  stream << "actions: " << ob.ptr->actions  <<'\n';
  stream << "attackCost: " << ob.ptr->attackCost  <<'\n';
  stream << "damage: " << ob.ptr->damage  <<'\n';
  stream << "minRange: " << ob.ptr->minRange  <<'\n';
  stream << "maxRange: " << ob.ptr->maxRange  <<'\n';
  stream << "trainerID: " << ob.ptr->trainerID  <<'\n';
  stream << "canPaint: " << ob.ptr->canPaint  <<'\n';
  stream << "armorExp: " << ob.ptr->armorExp  <<'\n';
  stream << "hpExp: " << ob.ptr->hpExp  <<'\n';
  stream << "priceExp: " << ob.ptr->priceExp  <<'\n';
  stream << "damageExp: " << ob.ptr->damageExp  <<'\n';
  stream << "paintBase: " << ob.ptr->paintBase  <<'\n';
  stream << "paintLinear: " << ob.ptr->paintLinear  <<'\n';
  return stream;
}


#include "getters.h"

int buildingGetObjectID(_Building* ptr)
{
  return ptr->objectID;
}
int buildingGetX(_Building* ptr)
{
  return ptr->x;
}
int buildingGetY(_Building* ptr)
{
  return ptr->y;
}
int buildingGetZ(_Building* ptr)
{
  return ptr->z;
}
int buildingGetHp(_Building* ptr)
{
  return ptr->hp;
}
int buildingGetLevel(_Building* ptr)
{
  return ptr->level;
}
int buildingGetBuildingTypeID(_Building* ptr)
{
  return ptr->buildingTypeID;
}
int buildingGetOwnerID(_Building* ptr)
{
  return ptr->ownerID;
}
int buildingGetInTraining(_Building* ptr)
{
  return ptr->inTraining;
}
int buildingGetProgress(_Building* ptr)
{
  return ptr->progress;
}
int buildingGetLinked(_Building* ptr)
{
  return ptr->linked;
}
int buildingGetComplete(_Building* ptr)
{
  return ptr->complete;
}
int buildingTypeGetObjectID(_BuildingType* ptr)
{
  return ptr->objectID;
}
char* buildingTypeGetName(_BuildingType* ptr)
{
  return ptr->name;
}
int buildingTypeGetPrice(_BuildingType* ptr)
{
  return ptr->price;
}
int buildingTypeGetFood(_BuildingType* ptr)
{
  return ptr->food;
}
int buildingTypeGetPastBuildTime(_BuildingType* ptr)
{
  return ptr->pastBuildTime;
}
int buildingTypeGetPresentBuildTime(_BuildingType* ptr)
{
  return ptr->presentBuildTime;
}
int buildingTypeGetFutureBuildTime(_BuildingType* ptr)
{
  return ptr->futureBuildTime;
}
int buildingTypeGetHp(_BuildingType* ptr)
{
  return ptr->hp;
}
int buildingTypeGetArmor(_BuildingType* ptr)
{
  return ptr->armor;
}
int buildingTypeGetBuilderID(_BuildingType* ptr)
{
  return ptr->builderID;
}
int buildingTypeGetAllowPaint(_BuildingType* ptr)
{
  return ptr->allowPaint;
}
int buildingTypeGetWidth(_BuildingType* ptr)
{
  return ptr->width;
}
int buildingTypeGetHeight(_BuildingType* ptr)
{
  return ptr->height;
}
int buildingTypeGetSpawnX(_BuildingType* ptr)
{
  return ptr->spawnX;
}
int buildingTypeGetSpawnY(_BuildingType* ptr)
{
  return ptr->spawnY;
}
float buildingTypeGetArmorExp(_BuildingType* ptr)
{
  return ptr->armorExp;
}
float buildingTypeGetHpExp(_BuildingType* ptr)
{
  return ptr->hpExp;
}
float buildingTypeGetPriceExp(_BuildingType* ptr)
{
  return ptr->priceExp;
}
float buildingTypeGetFoodExp(_BuildingType* ptr)
{
  return ptr->foodExp;
}
int portalGetObjectID(_Portal* ptr)
{
  return ptr->objectID;
}
int portalGetX(_Portal* ptr)
{
  return ptr->x;
}
int portalGetY(_Portal* ptr)
{
  return ptr->y;
}
int portalGetZ(_Portal* ptr)
{
  return ptr->z;
}
int portalGetDirection(_Portal* ptr)
{
  return ptr->direction;
}
int portalGetFee(_Portal* ptr)
{
  return ptr->fee;
}
int portalGetFeeIncr(_Portal* ptr)
{
  return ptr->feeIncr;
}
float portalGetFeeMultiplier(_Portal* ptr)
{
  return ptr->feeMultiplier;
}
int terrainGetObjectID(_Terrain* ptr)
{
  return ptr->objectID;
}
int terrainGetX(_Terrain* ptr)
{
  return ptr->x;
}
int terrainGetY(_Terrain* ptr)
{
  return ptr->y;
}
int terrainGetZ(_Terrain* ptr)
{
  return ptr->z;
}
int terrainGetBlocksMove(_Terrain* ptr)
{
  return ptr->blocksMove;
}
int terrainGetBlocksBuild(_Terrain* ptr)
{
  return ptr->blocksBuild;
}
int unitGetObjectID(_Unit* ptr)
{
  return ptr->objectID;
}
int unitGetX(_Unit* ptr)
{
  return ptr->x;
}
int unitGetY(_Unit* ptr)
{
  return ptr->y;
}
int unitGetZ(_Unit* ptr)
{
  return ptr->z;
}
int unitGetHp(_Unit* ptr)
{
  return ptr->hp;
}
int unitGetLevel(_Unit* ptr)
{
  return ptr->level;
}
int unitGetUnitTypeID(_Unit* ptr)
{
  return ptr->unitTypeID;
}
int unitGetOwnerID(_Unit* ptr)
{
  return ptr->ownerID;
}
int unitGetActions(_Unit* ptr)
{
  return ptr->actions;
}
int unitGetMoves(_Unit* ptr)
{
  return ptr->moves;
}
int unitTypeGetObjectID(_UnitType* ptr)
{
  return ptr->objectID;
}
char* unitTypeGetName(_UnitType* ptr)
{
  return ptr->name;
}
int unitTypeGetPrice(_UnitType* ptr)
{
  return ptr->price;
}
int unitTypeGetHunger(_UnitType* ptr)
{
  return ptr->hunger;
}
int unitTypeGetTrainTime(_UnitType* ptr)
{
  return ptr->trainTime;
}
int unitTypeGetHp(_UnitType* ptr)
{
  return ptr->hp;
}
int unitTypeGetArmor(_UnitType* ptr)
{
  return ptr->armor;
}
int unitTypeGetMoves(_UnitType* ptr)
{
  return ptr->moves;
}
int unitTypeGetActions(_UnitType* ptr)
{
  return ptr->actions;
}
int unitTypeGetAttackCost(_UnitType* ptr)
{
  return ptr->attackCost;
}
int unitTypeGetDamage(_UnitType* ptr)
{
  return ptr->damage;
}
int unitTypeGetMinRange(_UnitType* ptr)
{
  return ptr->minRange;
}
int unitTypeGetMaxRange(_UnitType* ptr)
{
  return ptr->maxRange;
}
int unitTypeGetTrainerID(_UnitType* ptr)
{
  return ptr->trainerID;
}
int unitTypeGetCanPaint(_UnitType* ptr)
{
  return ptr->canPaint;
}
float unitTypeGetArmorExp(_UnitType* ptr)
{
  return ptr->armorExp;
}
float unitTypeGetHpExp(_UnitType* ptr)
{
  return ptr->hpExp;
}
float unitTypeGetPriceExp(_UnitType* ptr)
{
  return ptr->priceExp;
}
float unitTypeGetDamageExp(_UnitType* ptr)
{
  return ptr->damageExp;
}
int unitTypeGetPaintBase(_UnitType* ptr)
{
  return ptr->paintBase;
}
int unitTypeGetPaintLinear(_UnitType* ptr)
{
  return ptr->paintLinear;
}


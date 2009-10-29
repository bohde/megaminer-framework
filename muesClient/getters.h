#ifndef GETTERS_H 
#define GETTERS_H
#include "structures.h"

#ifdef __cplusplus
extern "C" {
#endif

int buildingGetObjectID(_Building* ptr);
int buildingGetX(_Building* ptr);
int buildingGetY(_Building* ptr);
int buildingGetZ(_Building* ptr);
int buildingGetHp(_Building* ptr);
int buildingGetLevel(_Building* ptr);
int buildingGetBuildingTypeID(_Building* ptr);
int buildingGetOwnerID(_Building* ptr);
int buildingGetInTraining(_Building* ptr);
int buildingGetProgress(_Building* ptr);
int buildingGetLinked(_Building* ptr);
int buildingGetComplete(_Building* ptr);
int buildingTypeGetObjectID(_BuildingType* ptr);
char* buildingTypeGetName(_BuildingType* ptr);
int buildingTypeGetPrice(_BuildingType* ptr);
int buildingTypeGetFood(_BuildingType* ptr);
int buildingTypeGetPastBuildTime(_BuildingType* ptr);
int buildingTypeGetPresentBuildTime(_BuildingType* ptr);
int buildingTypeGetFutureBuildTime(_BuildingType* ptr);
int buildingTypeGetHp(_BuildingType* ptr);
int buildingTypeGetArmor(_BuildingType* ptr);
int buildingTypeGetBuilderID(_BuildingType* ptr);
int buildingTypeGetAllowPaint(_BuildingType* ptr);
int buildingTypeGetWidth(_BuildingType* ptr);
int buildingTypeGetHeight(_BuildingType* ptr);
int buildingTypeGetSpawnX(_BuildingType* ptr);
int buildingTypeGetSpawnY(_BuildingType* ptr);
float buildingTypeGetArmorExp(_BuildingType* ptr);
float buildingTypeGetHpExp(_BuildingType* ptr);
float buildingTypeGetPriceExp(_BuildingType* ptr);
float buildingTypeGetFoodExp(_BuildingType* ptr);
int portalGetObjectID(_Portal* ptr);
int portalGetX(_Portal* ptr);
int portalGetY(_Portal* ptr);
int portalGetZ(_Portal* ptr);
int portalGetDirection(_Portal* ptr);
int portalGetFee(_Portal* ptr);
int terrainGetObjectID(_Terrain* ptr);
int terrainGetX(_Terrain* ptr);
int terrainGetY(_Terrain* ptr);
int terrainGetZ(_Terrain* ptr);
int terrainGetBlockmove(_Terrain* ptr);
int terrainGetBlockbuild(_Terrain* ptr);
int unitGetObjectID(_Unit* ptr);
int unitGetX(_Unit* ptr);
int unitGetY(_Unit* ptr);
int unitGetZ(_Unit* ptr);
int unitGetHp(_Unit* ptr);
int unitGetLevel(_Unit* ptr);
int unitGetUnitTypeID(_Unit* ptr);
int unitGetOwnerID(_Unit* ptr);
int unitGetActions(_Unit* ptr);
int unitGetMoves(_Unit* ptr);
int unitTypeGetObjectID(_UnitType* ptr);
char* unitTypeGetName(_UnitType* ptr);
int unitTypeGetPrice(_UnitType* ptr);
int unitTypeGetHunger(_UnitType* ptr);
int unitTypeGetTraintime(_UnitType* ptr);
int unitTypeGetHp(_UnitType* ptr);
int unitTypeGetArmor(_UnitType* ptr);
int unitTypeGetMoves(_UnitType* ptr);
int unitTypeGetActions(_UnitType* ptr);
int unitTypeGetAttackcost(_UnitType* ptr);
int unitTypeGetDamage(_UnitType* ptr);
int unitTypeGetMinrange(_UnitType* ptr);
int unitTypeGetMaxrange(_UnitType* ptr);
int unitTypeGetTrainerID(_UnitType* ptr);
int unitTypeGetCanpaint(_UnitType* ptr);
float unitTypeGetArmorExp(_UnitType* ptr);
float unitTypeGetHpExp(_UnitType* ptr);
float unitTypeGetPriceExp(_UnitType* ptr);
float unitTypeGetDamageExp(_UnitType* ptr);
int unitTypeGetPaintBase(_UnitType* ptr);
int unitTypeGetPaintLinear(_UnitType* ptr);

#ifdef __cplusplus
}
#endif

#endif

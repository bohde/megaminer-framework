# -*-python-*-

import os

from ctypes import *

try:
  if os.name == 'posix':
    library = CDLL("../c/libclient.so")
  elif os.name == 'nt':
    library = CDLL("../c/client.dll")
  else:
    raise Exception("Unrecognized OS: "+os.name)
except OSError:
  raise Exception("It looks like you didn't build libclient. Run 'make' and try again.")

# convenience functions
library.getTypeFromUnit.restype = c_void_p
library.getTypeFromUnit.argtypes = [c_void_p]

library.getTypeFromBuilding.restype = c_void_p
library.getTypeFromBuilding.argtypes = [c_void_p]

library.canMove.restype = c_bool
library.canMove.argtypes = [c_int, c_int, c_int]

library.canBuild.restype = c_bool
library.canBuild.argtypes = [c_int, c_int, c_int]

library.effDamage.restype = c_int
library.effDamage.argtypes = [c_void_p, c_int]

library.effFood.restype = c_int
library.effFood.argtypes = [c_void_p, c_int]

library.getGold.restype = c_int
library.getGold.argtypes = [c_int, c_int]

library.artWorth.restype = c_int
library.artWorth.argtypes = [c_int, c_int]

library.hunger.restype = c_int
library.hunger.argtypes = [c_int, c_int]

library.foodProduced.restype = c_int
library.foodProduced.argtypes = [c_int, c_int]

library.effBuildingPrice.restype = c_int
library.effBuildingPrice.argtypes = [c_void_p, c_int]

library.effUnitPrice.restype = c_int
library.effUnitPrice.argtypes = [c_void_p, c_int]

library.effMaxHP.restype = c_int
library.effMaxHP.argtypes = [c_void_p, c_int]

library.effBuildingArmor.restype = c_int
library.effBuildingArmor.argtypes = [c_void_p, c_int]

library.effUnitArmor.restype = c_int
library.effUnitArmor.argtypes = [c_void_p, c_int]

# commands

library.serverLogin.restype = c_bool
library.serverLogin.argtypes = [c_int, c_char_p, c_char_p]

library.createGame.restype = c_int
library.createGame.argtypes = []

library.joinGame.restype = c_int
library.joinGame.argtypes = [c_int]

library.endTurn.restype = None
library.endTurn.argtypes = []

library.getStatus.restype = None
library.getStatus.argtypes = []

library.networkLoop.restype = c_int
library.networkLoop.argtypes = [c_int]

library.buildingTrain.restype = c_bool
library.buildingTrain.argtypes = [c_void_p, c_void_p]

library.buildingCancel.restype = c_bool
library.buildingCancel.argtypes = [c_void_p]

library.unitAttack.restype = c_bool
library.unitAttack.argtypes = [c_void_p, c_int, c_int]

library.unitBuild.restype = c_bool
library.unitBuild.argtypes = [c_void_p, c_int, c_int, c_void_p]

library.unitPaint.restype = c_bool
library.unitPaint.argtypes = [c_void_p, c_int, c_int]

library.unitMove.restype = c_bool
library.unitMove.argtypes = [c_void_p, c_int, c_int]

library.unitWarp.restype = c_bool
library.unitWarp.argtypes = [c_void_p]

# accessors

library.getMaxX.restype = c_int
library.getMaxX.argtypes = []

library.getMaxY.restype = c_int
library.getMaxY.argtypes = []

library.getPlayer0Gold0.restype = c_int
library.getPlayer0Gold0.argtypes = []

library.getPlayer0Gold1.restype = c_int
library.getPlayer0Gold1.argtypes = []

library.getPlayer0Gold2.restype = c_int
library.getPlayer0Gold2.argtypes = []

library.getPlayer1Gold0.restype = c_int
library.getPlayer1Gold0.argtypes = []

library.getPlayer1Gold1.restype = c_int
library.getPlayer1Gold1.argtypes = []

library.getPlayer1Gold2.restype = c_int
library.getPlayer1Gold2.argtypes = []

library.getPlayerID.restype = c_int
library.getPlayerID.argtypes = []

library.getTurnNumber.restype = c_int
library.getTurnNumber.argtypes = []

library.getBuilding.restype = c_void_p
library.getBuilding.argtypes = [c_int]

library.getBuildingCount.restype = c_int
library.getBuildingCount.argtypes = []

library.getBuildingType.restype = c_void_p
library.getBuildingType.argtypes = [c_int]

library.getBuildingTypeCount.restype = c_int
library.getBuildingTypeCount.argtypes = []

library.getPortal.restype = c_void_p
library.getPortal.argtypes = [c_int]

library.getPortalCount.restype = c_int
library.getPortalCount.argtypes = []

library.getTerrain.restype = c_void_p
library.getTerrain.argtypes = [c_int]

library.getTerrainCount.restype = c_int
library.getTerrainCount.argtypes = []

library.getUnit.restype = c_void_p
library.getUnit.argtypes = [c_int]

library.getUnitCount.restype = c_int
library.getUnitCount.argtypes = []

library.getUnitType.restype = c_void_p
library.getUnitType.argtypes = [c_int]

library.getUnitTypeCount.restype = c_int
library.getUnitTypeCount.argtypes = []

# getters

library.buildingGetObjectID.restype = c_int
library.buildingGetObjectID.argtypes = [c_void_p]

library.buildingGetX.restype = c_int
library.buildingGetX.argtypes = [c_void_p]

library.buildingGetY.restype = c_int
library.buildingGetY.argtypes = [c_void_p]

library.buildingGetZ.restype = c_int
library.buildingGetZ.argtypes = [c_void_p]

library.buildingGetHp.restype = c_int
library.buildingGetHp.argtypes = [c_void_p]

library.buildingGetLevel.restype = c_int
library.buildingGetLevel.argtypes = [c_void_p]

library.buildingGetBuildingTypeID.restype = c_int
library.buildingGetBuildingTypeID.argtypes = [c_void_p]

library.buildingGetOwnerID.restype = c_int
library.buildingGetOwnerID.argtypes = [c_void_p]

library.buildingGetInTraining.restype = c_int
library.buildingGetInTraining.argtypes = [c_void_p]

library.buildingGetProgress.restype = c_int
library.buildingGetProgress.argtypes = [c_void_p]

library.buildingGetLinked.restype = c_int
library.buildingGetLinked.argtypes = [c_void_p]

library.buildingGetComplete.restype = c_int
library.buildingGetComplete.argtypes = [c_void_p]

library.buildingTypeGetObjectID.restype = c_int
library.buildingTypeGetObjectID.argtypes = [c_void_p]

library.buildingTypeGetName.restype = c_char_p
library.buildingTypeGetName.argtypes = [c_void_p]

library.buildingTypeGetPrice.restype = c_int
library.buildingTypeGetPrice.argtypes = [c_void_p]

library.buildingTypeGetFood.restype = c_int
library.buildingTypeGetFood.argtypes = [c_void_p]

library.buildingTypeGetPastBuildTime.restype = c_int
library.buildingTypeGetPastBuildTime.argtypes = [c_void_p]

library.buildingTypeGetPresentBuildTime.restype = c_int
library.buildingTypeGetPresentBuildTime.argtypes = [c_void_p]

library.buildingTypeGetFutureBuildTime.restype = c_int
library.buildingTypeGetFutureBuildTime.argtypes = [c_void_p]

library.buildingTypeGetHp.restype = c_int
library.buildingTypeGetHp.argtypes = [c_void_p]

library.buildingTypeGetArmor.restype = c_int
library.buildingTypeGetArmor.argtypes = [c_void_p]

library.buildingTypeGetBuilderID.restype = c_int
library.buildingTypeGetBuilderID.argtypes = [c_void_p]

library.buildingTypeGetAllowPaint.restype = c_int
library.buildingTypeGetAllowPaint.argtypes = [c_void_p]

library.buildingTypeGetWidth.restype = c_int
library.buildingTypeGetWidth.argtypes = [c_void_p]

library.buildingTypeGetHeight.restype = c_int
library.buildingTypeGetHeight.argtypes = [c_void_p]

library.buildingTypeGetSpawnX.restype = c_int
library.buildingTypeGetSpawnX.argtypes = [c_void_p]

library.buildingTypeGetSpawnY.restype = c_int
library.buildingTypeGetSpawnY.argtypes = [c_void_p]

library.buildingTypeGetArmorExp.restype = c_float
library.buildingTypeGetArmorExp.argtypes = [c_void_p]

library.buildingTypeGetHpExp.restype = c_float
library.buildingTypeGetHpExp.argtypes = [c_void_p]

library.buildingTypeGetPriceExp.restype = c_float
library.buildingTypeGetPriceExp.argtypes = [c_void_p]

library.buildingTypeGetFoodExp.restype = c_float
library.buildingTypeGetFoodExp.argtypes = [c_void_p]

library.portalGetObjectID.restype = c_int
library.portalGetObjectID.argtypes = [c_void_p]

library.portalGetX.restype = c_int
library.portalGetX.argtypes = [c_void_p]

library.portalGetY.restype = c_int
library.portalGetY.argtypes = [c_void_p]

library.portalGetZ.restype = c_int
library.portalGetZ.argtypes = [c_void_p]

library.portalGetDirection.restype = c_int
library.portalGetDirection.argtypes = [c_void_p]

library.portalGetFee.restype = c_int
library.portalGetFee.argtypes = [c_void_p]

library.portalGetFeeIncr.restype = c_int
library.portalGetFeeIncr.argtypes = [c_void_p]

library.portalGetFeeMultiplier.restype = c_float
library.portalGetFeeMultiplier.argtypes = [c_void_p]

library.terrainGetObjectID.restype = c_int
library.terrainGetObjectID.argtypes = [c_void_p]

library.terrainGetX.restype = c_int
library.terrainGetX.argtypes = [c_void_p]

library.terrainGetY.restype = c_int
library.terrainGetY.argtypes = [c_void_p]

library.terrainGetZ.restype = c_int
library.terrainGetZ.argtypes = [c_void_p]

library.terrainGetBlocksMove.restype = c_int
library.terrainGetBlocksMove.argtypes = [c_void_p]

library.terrainGetBlocksBuild.restype = c_int
library.terrainGetBlocksBuild.argtypes = [c_void_p]

library.unitGetObjectID.restype = c_int
library.unitGetObjectID.argtypes = [c_void_p]

library.unitGetX.restype = c_int
library.unitGetX.argtypes = [c_void_p]

library.unitGetY.restype = c_int
library.unitGetY.argtypes = [c_void_p]

library.unitGetZ.restype = c_int
library.unitGetZ.argtypes = [c_void_p]

library.unitGetHp.restype = c_int
library.unitGetHp.argtypes = [c_void_p]

library.unitGetLevel.restype = c_int
library.unitGetLevel.argtypes = [c_void_p]

library.unitGetUnitTypeID.restype = c_int
library.unitGetUnitTypeID.argtypes = [c_void_p]

library.unitGetOwnerID.restype = c_int
library.unitGetOwnerID.argtypes = [c_void_p]

library.unitGetActions.restype = c_int
library.unitGetActions.argtypes = [c_void_p]

library.unitGetMoves.restype = c_int
library.unitGetMoves.argtypes = [c_void_p]

library.unitTypeGetObjectID.restype = c_int
library.unitTypeGetObjectID.argtypes = [c_void_p]

library.unitTypeGetName.restype = c_char_p
library.unitTypeGetName.argtypes = [c_void_p]

library.unitTypeGetPrice.restype = c_int
library.unitTypeGetPrice.argtypes = [c_void_p]

library.unitTypeGetHunger.restype = c_int
library.unitTypeGetHunger.argtypes = [c_void_p]

library.unitTypeGetTrainTime.restype = c_int
library.unitTypeGetTrainTime.argtypes = [c_void_p]

library.unitTypeGetHp.restype = c_int
library.unitTypeGetHp.argtypes = [c_void_p]

library.unitTypeGetArmor.restype = c_int
library.unitTypeGetArmor.argtypes = [c_void_p]

library.unitTypeGetMoves.restype = c_int
library.unitTypeGetMoves.argtypes = [c_void_p]

library.unitTypeGetActions.restype = c_int
library.unitTypeGetActions.argtypes = [c_void_p]

library.unitTypeGetAttackCost.restype = c_int
library.unitTypeGetAttackCost.argtypes = [c_void_p]

library.unitTypeGetDamage.restype = c_int
library.unitTypeGetDamage.argtypes = [c_void_p]

library.unitTypeGetMinRange.restype = c_int
library.unitTypeGetMinRange.argtypes = [c_void_p]

library.unitTypeGetMaxRange.restype = c_int
library.unitTypeGetMaxRange.argtypes = [c_void_p]

library.unitTypeGetTrainerID.restype = c_int
library.unitTypeGetTrainerID.argtypes = [c_void_p]

library.unitTypeGetCanPaint.restype = c_int
library.unitTypeGetCanPaint.argtypes = [c_void_p]

library.unitTypeGetArmorExp.restype = c_float
library.unitTypeGetArmorExp.argtypes = [c_void_p]

library.unitTypeGetHpExp.restype = c_float
library.unitTypeGetHpExp.argtypes = [c_void_p]

library.unitTypeGetPriceExp.restype = c_float
library.unitTypeGetPriceExp.argtypes = [c_void_p]

library.unitTypeGetDamageExp.restype = c_float
library.unitTypeGetDamageExp.argtypes = [c_void_p]

library.unitTypeGetPaintBase.restype = c_int
library.unitTypeGetPaintBase.argtypes = [c_void_p]

library.unitTypeGetPaintLinear.restype = c_int
library.unitTypeGetPaintLinear.argtypes = [c_void_p]


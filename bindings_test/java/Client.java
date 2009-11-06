import com.sun.jna.Library;
import com.sun.jna.Pointer;
import com.sun.jna.Native;

public interface Client extends Library {
    Client INSTANCE = (Client)Native.loadLibrary("client", Client.class);
    int open_server_connection(String host, String port);

    boolean serverLogin(int socket, String username, String password);
    int createGame();
    int joinGame(int id);

    void endTurn();
    void getStatus();

    int networkLoop(int socket);


    //commands
    boolean buildingTrain(Pointer object, Pointer unit);
    boolean buildingCancel(Pointer object);
    boolean unitAttack(Pointer object, int x, int y);
    boolean unitBuild(Pointer object, int x, int y, Pointer type);
    boolean unitPaint(Pointer object, int x, int y);
    boolean unitMove(Pointer object, int x, int y);
    boolean unitWarp(Pointer object);

    //accessors
    int getMaxX();
    int getMaxY();
    int getPlayer0Gold0();
    int getPlayer0Gold1();
    int getPlayer0Gold2();
    int getPlayer1Gold0();
    int getPlayer1Gold1();
    int getPlayer1Gold2();
    int getPlayerID();
    int getTurnNumber();

    Pointer getBuilding(int num);
    int getBuildingCount();
    Pointer getBuildingType(int num);
    int getBuildingTypeCount();
    Pointer getPortal(int num);
    int getPortalCount();
    Pointer getTerrain(int num);
    int getTerrainCount();
    Pointer getUnit(int num);
    int getUnitCount();
    Pointer getUnitType(int num);
    int getUnitTypeCount();

    // Convenience functions
    UnitType getTypeFromUnit(Unit u);
    BuildingType getTypeFromBuilding(Building b);
    boolean canMove(int x, int y, int z);
    boolean canBuild(int x, int y, int z);
    int effDamage(UnitType ut, int level);
    int effFood(BuildingType bt, int level);
    int getGold(int playerNum, int z);
    int artWorth(int artistLevel, int galleryLevel);
    int hunger(int playerID, int z);
    int foodProduced(int playerID, int z);
    int effBuildingPrice(BuildingType bt, int level);
    int effUnitPrice(BuildingType bt, int level);
    int effMaxHP(UnitType ut, int level);
    int effArmor(BuildingType bt, int level);

    //getters
    int buildingGetObjectID(Pointer ptr);
    int buildingGetX(Pointer ptr);
    int buildingGetY(Pointer ptr);
    int buildingGetZ(Pointer ptr);
    int buildingGetHp(Pointer ptr);
    int buildingGetLevel(Pointer ptr);
    int buildingGetBuildingTypeID(Pointer ptr);
    int buildingGetOwnerID(Pointer ptr);
    int buildingGetInTraining(Pointer ptr);
    int buildingGetProgress(Pointer ptr);
    int buildingGetLinked(Pointer ptr);
    int buildingGetComplete(Pointer ptr);

    int buildingTypeGetObjectID(Pointer ptr);
    String buildingTypeGetName(Pointer ptr);
    int buildingTypeGetPrice(Pointer ptr);
    int buildingTypeGetFood(Pointer ptr);
    int buildingTypeGetPastBuildTime(Pointer ptr);
    int buildingTypeGetPresentBuildTime(Pointer ptr);
    int buildingTypeGetFutureBuildTime(Pointer ptr);
    int buildingTypeGetHp(Pointer ptr);
    int buildingTypeGetArmor(Pointer ptr);
    int buildingTypeGetBuilderID(Pointer ptr);
    int buildingTypeGetAllowPaint(Pointer ptr);
    int buildingTypeGetWidth(Pointer ptr);
    int buildingTypeGetHeight(Pointer ptr);
    int buildingTypeGetSpawnX(Pointer ptr);
    int buildingTypeGetSpawnY(Pointer ptr);
    float buildingTypeGetArmorExp(Pointer ptr);
    float buildingTypeGetHpExp(Pointer ptr);
    float buildingTypeGetPriceExp(Pointer ptr);
    float buildingTypeGetFoodExp(Pointer ptr);

    int portalGetObjectID(Pointer ptr);
    int portalGetX(Pointer ptr);
    int portalGetY(Pointer ptr);
    int portalGetZ(Pointer ptr);
    int portalGetDirection(Pointer ptr);
    int portalGetFee(Pointer ptr);
    int portalGetFeeIncr(Pointer ptr);
    float portalGetFeeMultiplier(Pointer ptr);

    int terrainGetObjectID(Pointer ptr);
    int terrainGetX(Pointer ptr);
    int terrainGetY(Pointer ptr);
    int terrainGetZ(Pointer ptr);
    int terrainGetBlocksMove(Pointer ptr);
    int terrainGetBlocksBuild(Pointer ptr);

    int unitGetObjectID(Pointer ptr);
    int unitGetX(Pointer ptr);
    int unitGetY(Pointer ptr);
    int unitGetZ(Pointer ptr);
    int unitGetHp(Pointer ptr);
    int unitGetLevel(Pointer ptr);
    int unitGetUnitTypeID(Pointer ptr);
    int unitGetOwnerID(Pointer ptr);
    int unitGetActions(Pointer ptr);
    int unitGetMoves(Pointer ptr);

    int unitTypeGetObjectID(Pointer ptr);
    String unitTypeGetName(Pointer ptr);
    int unitTypeGetPrice(Pointer ptr);
    int unitTypeGetHunger(Pointer ptr);
    int unitTypeGetTrainTime(Pointer ptr);
    int unitTypeGetHp(Pointer ptr);
    int unitTypeGetArmor(Pointer ptr);
    int unitTypeGetMoves(Pointer ptr);
    int unitTypeGetActions(Pointer ptr);
    int unitTypeGetAttackCost(Pointer ptr);
    int unitTypeGetDamage(Pointer ptr);
    int unitTypeGetMinRange(Pointer ptr);
    int unitTypeGetMaxRange(Pointer ptr);
    int unitTypeGetTrainerID(Pointer ptr);
    int unitTypeGetCanPaint(Pointer ptr);
    float unitTypeGetArmorExp(Pointer ptr);
    float unitTypeGetHpExp(Pointer ptr);
    float unitTypeGetPriceExp(Pointer ptr);
    float unitTypeGetDamageExp(Pointer ptr);
    int unitTypeGetPaintBase(Pointer ptr);
    int unitTypeGetPaintLinear(Pointer ptr);


}

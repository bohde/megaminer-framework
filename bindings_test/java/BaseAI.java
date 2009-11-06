
/// \brief A basic AI interface.

///This class implements most the code an AI would need to interface with the lower-level game code.
///AIs should extend this class to get a lot of builer-plate code out of the way
///The provided AI class does just that.
public abstract class BaseAI
{
    static Building[] buildings;
    static BuildingType[] buildingTypes;
    static Portal[] portals;
    static Terrain[] terrains;
    static Unit[] units;
    static UnitType[] unitTypes;
    static int iteration;
    boolean initialized;
    
    ///
    ///Make this your username, which should be provided.
    public abstract String username();
    ///
    ///Make this your password, which should be provided.
    public abstract String password();
    ///
    ///This is run on turn 1 before run
    public abstract void init();
    ///
    ///This is run every turn . Return true to end the turn, return false
    ///to request a status update from the server and then immediately rerun this function with the
    ///latest game status.
    public abstract boolean run();

    public boolean startTurn()
    {
        int count = 0;
        count = Client.INSTANCE.getBuildingCount();
        buildings = new Building[count];
        for(int i = 0; i < count; i++)
        {
            buildings[i] = new Building(Client.INSTANCE.getBuilding(i));
        }
        count = Client.INSTANCE.getBuildingTypeCount();
        buildingTypes = new BuildingType[count];
        for(int i = 0; i < count; i++)
        {
            buildingTypes[i] = new BuildingType(Client.INSTANCE.getBuildingType(i));
        }
        count = Client.INSTANCE.getPortalCount();
        portals = new Portal[count];
        for(int i = 0; i < count; i++)
        {
            portals[i] = new Portal(Client.INSTANCE.getPortal(i));
        }
        count = Client.INSTANCE.getTerrainCount();
        terrains = new Terrain[count];
        for(int i = 0; i < count; i++)
        {
            terrains[i] = new Terrain(Client.INSTANCE.getTerrain(i));
        }
        count = Client.INSTANCE.getUnitCount();
        units = new Unit[count];
        for(int i = 0; i < count; i++)
        {
            units[i] = new Unit(Client.INSTANCE.getUnit(i));
        }
        count = Client.INSTANCE.getUnitTypeCount();
        unitTypes = new UnitType[count];
        for(int i = 0; i < count; i++)
        {
            unitTypes[i] = new UnitType(Client.INSTANCE.getUnitType(i));
        }

        iteration++;

        if(!initialized)
        {
          initialized = true;
          init();
        }
        return run();
    }


    int maxX()
    {
        return Client.INSTANCE.getMaxX();
    }
    int maxY()
    {
        return Client.INSTANCE.getMaxY();
    }
    ///Player 0's past gold
    int player0Gold0()
    {
        return Client.INSTANCE.getPlayer0Gold0();
    }
    ///Player 0's present gold
    int player0Gold1()
    {
        return Client.INSTANCE.getPlayer0Gold1();
    }
    ///Player 0's future gold
    int player0Gold2()
    {
        return Client.INSTANCE.getPlayer0Gold2();
    }
    ///Player 1's past gold
    int player1Gold0()
    {
        return Client.INSTANCE.getPlayer1Gold0();
    }
    ///Player 1's present gold
    int player1Gold1()
    {
        return Client.INSTANCE.getPlayer1Gold1();
    }
    ///Player 1's future gold
    int player1Gold2()
    {
        return Client.INSTANCE.getPlayer1Gold2();
    }
    ///Player Number; either 0 or 2
    int playerID()
    {
        return Client.INSTANCE.getPlayerID();
    }
    int turnNumber()
    {
        return Client.INSTANCE.getTurnNumber();
    }

    ////////////////////////////////////////////
    // Convenience Functions
    ///////////////////////////////////////////
    UnitType getTypeFromUnit(Unit u) {
        return new UnitType(Client.INSTANCE.getTypeFromUnit(u.ptr));
    }

    BuildingType getTypeFromBuilding(Building b) {
        return new BuildingType(Client.INSTANCE.getTypeFromBuilding(b.ptr));
    }

    boolean canMove(int x, int y, int z) {
        return Client.INSTANCE.canMove(x, y, z);
    }

    boolean canBuild(int x, int y, int z) {
        return Client.INSTANCE.canBuild(x, y, z);
    }

    int effDamage(UnitType ut, int level) {
        return Client.INSTANCE.effDamage(ut.ptr, level);
    }

    int effFood(BuildingType bt, int level) {
        return Client.INSTANCE.effFood(bt.ptr, level);
    }

    int getGold(int playerNum, int z) {
        return Client.INSTANCE.getGold(playerNum, z);
    }

    int artWorth(int artistLevel, int galleryLevel) {
        return Client.INSTANCE.artWorth(artistLevel, galleryLevel);
    }

    int hunger(int playerID, int z) {
        return Client.INSTANCE.hunger(playerID, z);
    }

    int foodProduced(int playerID, int z) {
        return Client.INSTANCE.foodProduced(playerID, z);
    }

    int effBuildingPrice(BuildingType bt, int level) {
        return Client.INSTANCE.effBuildingPrice(bt.ptr, level);
    }

    int effUnitPrice(BuildingType bt, int level) {
        return Client.INSTANCE.effUnitPrice(bt.ptr, level);
    }

    int effMaxHP(UnitType ut, int level) {
        return Client.INSTANCE.effMaxHP(ut.ptr, level);
    }

    int effBuildingArmor(BuildingType bt, int level) {
        return Client.INSTANCE.effBuildingArmor(bt.ptr, level);
    }

    int effUnitArmor(UnitType ut, int level) {
        return Client.INSTANCE.effUnitArmor(ut.ptr, level);
    }
}

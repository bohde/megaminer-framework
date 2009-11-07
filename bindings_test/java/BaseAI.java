
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

///////////////////////////////////////////////////////////////
/// Gets the X boundary for the map in all time periods.
///
/// For each time period, the map is a rectangle from (-max_x,-max_y)
/// to (max_x,max_y)
///////////////////////////////////////////////////////////////
    int maxX()
    {
        return Client.INSTANCE.getMaxX();
    }

///////////////////////////////////////////////////////////////
/// Gets the Y boundary for the map in all time periods.
///
/// For each time period, the map is a rectangle from (-max_x,-max_y)
/// to (max_x,max_y)
///////////////////////////////////////////////////////////////
    int maxY()
    {
        return Client.INSTANCE.getMaxY();
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 0 has in the far past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
    int player0Gold0()
    {
        return Client.INSTANCE.getPlayer0Gold0();
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 0 has in the past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
    int player0Gold1()
    {
        return Client.INSTANCE.getPlayer0Gold1();
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 0 has in the present
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
    int player0Gold2()
    {
        return Client.INSTANCE.getPlayer0Gold2();
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 1 has in the far past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
    int player1Gold0()
    {
        return Client.INSTANCE.getPlayer1Gold0();
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 1 has in the past
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
    int player1Gold1()
    {
        return Client.INSTANCE.getPlayer1Gold1();
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold player 1 has in the present
/// Also see int BaseAI::getGold(int playerNum, int z)
///////////////////////////////////////////////////////////////
    int player1Gold2()
    {
        return Client.INSTANCE.getPlayer1Gold2();
    }

///////////////////////////////////////////////////////////////
/// Returns the your player ID, either 0 or 1.
///
/// This value will match the ownerID of all your units.
///////////////////////////////////////////////////////////////
    int playerID()
    {
        return Client.INSTANCE.getPlayerID();
    }

///////////////////////////////////////////////////////////////
/// Returns the current turn number
///
/// The first turn is turn 0.  Player 0 gets the first turn.
/// The second turn is turn 1.  Player 1 gets the first turn.
/// The game is ends at the end of turn 499 or earlier.
///////////////////////////////////////////////////////////////
    int turnNumber()
    {
        return Client.INSTANCE.getTurnNumber();
    }

    ////////////////////////////////////////////
    // Convenience Functions
    ///////////////////////////////////////////

///////////////////////////////////////////////////////////////
/// Returns the type of the given unit.
///////////////////////////////////////////////////////////////
    UnitType getTypeFromUnit(Unit u) {
        return new UnitType(Client.INSTANCE.getTypeFromUnit(u.ptr));
    }

///////////////////////////////////////////////////////////////
/// Returns the type of the given building.
///////////////////////////////////////////////////////////////
    BuildingType getTypeFromBuilding(Building b) {
        return new BuildingType(Client.INSTANCE.getTypeFromBuilding(b.ptr));
    }

///////////////////////////////////////////////////////////////
/// Returns true if one of your units could move to the given coordinate
///
/// This function checks to see if this square contains any enemy units,
/// enemy buildings, or blocking terrain.
/// This is not an efficient implementation.  Feel free to write your own.
///////////////////////////////////////////////////////////////
    boolean canMove(int x, int y, int z) {
        return Client.INSTANCE.canMove(x, y, z);
    }

///////////////////////////////////////////////////////////////
/// Returns true if this square is clear for you to build on.
///
/// This function checks to see if this square contains any enemy units,
/// buildings, or blocking terrain.
/// This is not an efficient implementation.  Feel free to write your own.
///////////////////////////////////////////////////////////////
    boolean canBuild(int x, int y, int z) {
        return Client.INSTANCE.canBuild(x, y, z);
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of raw damage a given type of unit would cause
/// at the given level.
///////////////////////////////////////////////////////////////
    int effDamage(UnitType ut, int level) {
        return Client.INSTANCE.effDamage(ut.ptr, level);
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of food produced by a given type of building
/// at the given level.
///////////////////////////////////////////////////////////////
    int effFood(BuildingType bt, int level) {
        return Client.INSTANCE.effFood(bt.ptr, level);
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold the given player has in the given
/// time period
///////////////////////////////////////////////////////////////
    int getGold(int playerNum, int z) {
        return Client.INSTANCE.getGold(playerNum, z);
    }

///////////////////////////////////////////////////////////////
/// Returns the amount of gold that would be gained if an artist
/// at the given level paints at a gallery of the given level.
///////////////////////////////////////////////////////////////
    int artWorth(int artistLevel, int galleryLevel) {
        return Client.INSTANCE.artWorth(artistLevel, galleryLevel);
    }

///////////////////////////////////////////////////////////////
/// Returns the sum of all hunger values for all units owned
/// by the given player in the given time period.
///////////////////////////////////////////////////////////////
    int hunger(int playerID, int z) {
        return Client.INSTANCE.hunger(playerID, z);
    }

///////////////////////////////////////////////////////////////
/// Returns the sum of all food produced by all buildings owned
/// by the given player in the given time period.
///////////////////////////////////////////////////////////////
    int foodProduced(int playerID, int z) {
        return Client.INSTANCE.foodProduced(playerID, z);
    }

///////////////////////////////////////////////////////////////
/// Returns the price of a building of the given type and level.
///////////////////////////////////////////////////////////////
    int effBuildingPrice(BuildingType bt, int level) {
        return Client.INSTANCE.effBuildingPrice(bt.ptr, level);
    }

///////////////////////////////////////////////////////////////
/// Returns the price of a unit of the given type and level.
///////////////////////////////////////////////////////////////
    int effUnitPrice(BuildingType bt, int level) {
        return Client.INSTANCE.effUnitPrice(bt.ptr, level);
    }

///////////////////////////////////////////////////////////////
/// Returns the maxHP of a building of the given type and level.
///////////////////////////////////////////////////////////////
    int effUnitMaxHP(UnitType ut, int level) {
        return Client.INSTANCE.effMaxHP(ut.ptr, level);
    }

///////////////////////////////////////////////////////////////
/// Returns the maxHP of a building of the given type and level.
///////////////////////////////////////////////////////////////
    int effBuildingMaxHP(BuildingType bt, int level) {
        return Client.INSTANCE.effBuildingMaxHP(bt.ptr, level);
    }

///////////////////////////////////////////////////////////////
/// Returns the armor of a building of the given type and level.
///////////////////////////////////////////////////////////////
    int effBuildingArmor(BuildingType bt, int level) {
        return Client.INSTANCE.effBuildingArmor(bt.ptr, level);
    }

///////////////////////////////////////////////////////////////
/// Returns the armor of a unit of the given type and level.
///////////////////////////////////////////////////////////////
    int effUnitArmor(UnitType ut, int level) {
        return Client.INSTANCE.effUnitArmor(ut.ptr, level);
    }
}

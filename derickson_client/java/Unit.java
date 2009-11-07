import com.sun.jna.Pointer;

///An entitiy that can move around the game and act.
class Unit
{
    Pointer ptr;
    int ID;
    int iteration;
    public Unit(Pointer p)
    {
            ptr = p;
            ID = Client.INSTANCE.unitGetObjectID(ptr);
            iteration = BaseAI.iteration;
    }

    boolean validify()
    {
        if(iteration == BaseAI.iteration) return true;
        for(int i = 0; i < BaseAI.units.length; i++)
        {
          if(BaseAI.units[i].ID == ID)
            {
                ptr = BaseAI.units[i].ptr;
                iteration = BaseAI.iteration;
                return true;
            }
        }
      throw new ExistentialError();
    }
    
    //commands
    
    boolean attack(int x, int y)
    {
        validify();
        return Client.INSTANCE.unitAttack(ptr, x, y);
    }
    boolean build(int x, int y, BuildingType type)
    {
        validify();
        type.validify();
        return Client.INSTANCE.unitBuild(ptr, x, y, type.ptr);
    }
    boolean paint(int x, int y)
    {
        validify();
        return Client.INSTANCE.unitPaint(ptr, x, y);
    }
    boolean move(int x, int y)
    {
        validify();
        return Client.INSTANCE.unitMove(ptr, x, y);
    }
    boolean warp()
    {
        validify();
        return Client.INSTANCE.unitWarp(ptr);
    }
    
    //getters
    
    public int getObjectID()
    {
        validify();
        return Client.INSTANCE.unitGetObjectID(ptr);
    }
    public int getX()
    {
        validify();
        return Client.INSTANCE.unitGetX(ptr);
    }
    public int getY()
    {
        validify();
        return Client.INSTANCE.unitGetY(ptr);
    }
    public int getZ()
    {
        validify();
        return Client.INSTANCE.unitGetZ(ptr);
    }
    public int getHp()
    {
        validify();
        return Client.INSTANCE.unitGetHp(ptr);
    }
    public int getLevel()
    {
        validify();
        return Client.INSTANCE.unitGetLevel(ptr);
    }
    public int getUnitTypeID()
    {
        validify();
        return Client.INSTANCE.unitGetUnitTypeID(ptr);
    }
    public int getOwnerID()
    {
        validify();
        return Client.INSTANCE.unitGetOwnerID(ptr);
    }
    public int getActions()
    {
        validify();
        return Client.INSTANCE.unitGetActions(ptr);
    }
    public int getMoves()
    {
        validify();
        return Client.INSTANCE.unitGetMoves(ptr);
    }
}

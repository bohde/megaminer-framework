import com.sun.jna.Pointer;

///This defines the attributes of a kind of unit.
class UnitType
{
    Pointer ptr;
    int ID;
    int iteration;
    public UnitType(Pointer p)
    {
            ptr = p;
            ID = Client.INSTANCE.unitTypeGetObjectID(ptr);
            iteration = BaseAI.iteration;
    }

    boolean validify()
    {
        if(iteration == BaseAI.iteration) return true;
        for(int i = 0; i < BaseAI.unitTypes.length; i++)
        {
          if(BaseAI.unitTypes[i].ID == ID)
            {
                ptr = BaseAI.unitTypes[i].ptr;
                iteration = BaseAI.iteration;
                return true;
            }
        }
      throw new ExistentialError();
    }
    
    //commands
    
    
    //getters
    
    public int getObjectID()
    {
        validify();
        return Client.INSTANCE.unitTypeGetObjectID(ptr);
    }
    public String getName()
    {
        validify();
        return Client.INSTANCE.unitTypeGetName(ptr);
    }
    public int getPrice()
    {
        validify();
        return Client.INSTANCE.unitTypeGetPrice(ptr);
    }
    public int getHunger()
    {
        validify();
        return Client.INSTANCE.unitTypeGetHunger(ptr);
    }
    public int getTrainTime()
    {
        validify();
        return Client.INSTANCE.unitTypeGetTrainTime(ptr);
    }
    public int getHp()
    {
        validify();
        return Client.INSTANCE.unitTypeGetHp(ptr);
    }
    public int getArmor()
    {
        validify();
        return Client.INSTANCE.unitTypeGetArmor(ptr);
    }
    public int getMoves()
    {
        validify();
        return Client.INSTANCE.unitTypeGetMoves(ptr);
    }
    public int getActions()
    {
        validify();
        return Client.INSTANCE.unitTypeGetActions(ptr);
    }
    public int getAttackCost()
    {
        validify();
        return Client.INSTANCE.unitTypeGetAttackCost(ptr);
    }
    public int getDamage()
    {
        validify();
        return Client.INSTANCE.unitTypeGetDamage(ptr);
    }
    public int getMinRange()
    {
        validify();
        return Client.INSTANCE.unitTypeGetMinRange(ptr);
    }
    public int getMaxRange()
    {
        validify();
        return Client.INSTANCE.unitTypeGetMaxRange(ptr);
    }
    public int getTrainerID()
    {
        validify();
        return Client.INSTANCE.unitTypeGetTrainerID(ptr);
    }
    public int getCanPaint()
    {
        validify();
        return Client.INSTANCE.unitTypeGetCanPaint(ptr);
    }
    public float getArmorExp()
    {
        validify();
        return Client.INSTANCE.unitTypeGetArmorExp(ptr);
    }
    public float getHpExp()
    {
        validify();
        return Client.INSTANCE.unitTypeGetHpExp(ptr);
    }
    public float getPriceExp()
    {
        validify();
        return Client.INSTANCE.unitTypeGetPriceExp(ptr);
    }
    public float getDamageExp()
    {
        validify();
        return Client.INSTANCE.unitTypeGetDamageExp(ptr);
    }
    public int getPaintBase()
    {
        validify();
        return Client.INSTANCE.unitTypeGetPaintBase(ptr);
    }
    public int getPaintLinear()
    {
        validify();
        return Client.INSTANCE.unitTypeGetPaintLinear(ptr);
    }
}

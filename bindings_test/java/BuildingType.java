import com.sun.jna.Pointer;

///This defines the attributes of a kind of building.
class BuildingType
{
    Pointer ptr;
    int ID;
    int iteration;
    public BuildingType(Pointer p)
    {
            ptr = p;
            ID = Client.INSTANCE.buildingTypeGetObjectID(ptr);
            iteration = BaseAI.iteration;
    }

    boolean validify()
    {
        if(iteration == BaseAI.iteration) return true;
        for(int i = 0; i < BaseAI.buildingTypes.length; i++)
        {
          if(BaseAI.buildingTypes[i].ID == ID)
            {
                ptr = BaseAI.buildingTypes[i].ptr;
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
        return Client.INSTANCE.buildingTypeGetObjectID(ptr);
    }
    public String getName()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetName(ptr);
    }
    public int getPrice()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetPrice(ptr);
    }
    public int getFood()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetFood(ptr);
    }
    public int getPastBuildTime()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetPastBuildTime(ptr);
    }
    public int getPresentBuildTime()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetPresentBuildTime(ptr);
    }
    public int getFutureBuildTime()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetFutureBuildTime(ptr);
    }
    public int getHp()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetHp(ptr);
    }
    public int getArmor()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetArmor(ptr);
    }
    public int getBuilderID()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetBuilderID(ptr);
    }
    public int getAllowPaint()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetAllowPaint(ptr);
    }
    public int getWidth()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetWidth(ptr);
    }
    public int getHeight()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetHeight(ptr);
    }
    public int getSpawnX()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetSpawnX(ptr);
    }
    public int getSpawnY()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetSpawnY(ptr);
    }
    public float getArmorExp()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetArmorExp(ptr);
    }
    public float getHpExp()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetHpExp(ptr);
    }
    public float getPriceExp()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetPriceExp(ptr);
    }
    public float getFoodExp()
    {
        validify();
        return Client.INSTANCE.buildingTypeGetFoodExp(ptr);
    }
}

import com.sun.jna.Pointer;

///A building to shelter, feed, and/or create units.
class Building
{
    Pointer ptr;
    int ID;
    int iteration;
    public Building(Pointer p)
    {
            ptr = p;
            ID = Client.INSTANCE.buildingGetObjectID(ptr);
            iteration = BaseAI.iteration;
    }

    boolean validify()
    {
        if(iteration == BaseAI.iteration) return true;
        for(int i = 0; i < BaseAI.buildings.length; i++)
        {
          if(BaseAI.buildings[i].ID == ID)
            {
                ptr = BaseAI.buildings[i].ptr;
                iteration = BaseAI.iteration;
                return true;
            }
        }
      throw new ExistentialError();
    }
    
    //commands
    
    boolean train(UnitType unit)
    {
        validify();
        unit.validify();
        return Client.INSTANCE.buildingTrain(ptr, unit.ptr);
    }
    boolean cancel()
    {
        validify();
        return Client.INSTANCE.buildingCancel(ptr);
    }
    
    //getters
    
    public int getObjectID()
    {
        validify();
        return Client.INSTANCE.buildingGetObjectID(ptr);
    }
    public int getX()
    {
        validify();
        return Client.INSTANCE.buildingGetX(ptr);
    }
    public int getY()
    {
        validify();
        return Client.INSTANCE.buildingGetY(ptr);
    }
    public int getZ()
    {
        validify();
        return Client.INSTANCE.buildingGetZ(ptr);
    }
    public int getHp()
    {
        validify();
        return Client.INSTANCE.buildingGetHp(ptr);
    }
    public int getLevel()
    {
        validify();
        return Client.INSTANCE.buildingGetLevel(ptr);
    }
    public int getBuildingTypeID()
    {
        validify();
        return Client.INSTANCE.buildingGetBuildingTypeID(ptr);
    }
    public int getOwnerID()
    {
        validify();
        return Client.INSTANCE.buildingGetOwnerID(ptr);
    }
    public int getInTraining()
    {
        validify();
        return Client.INSTANCE.buildingGetInTraining(ptr);
    }
    public int getProgress()
    {
        validify();
        return Client.INSTANCE.buildingGetProgress(ptr);
    }
    public int getLinked()
    {
        validify();
        return Client.INSTANCE.buildingGetLinked(ptr);
    }
    public int getComplete()
    {
        validify();
        return Client.INSTANCE.buildingGetComplete(ptr);
    }
}

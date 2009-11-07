import com.sun.jna.Pointer;

///A connection between two adjacent times.
class Portal
{
    Pointer ptr;
    int ID;
    int iteration;
    public Portal(Pointer p)
    {
            ptr = p;
            ID = Client.INSTANCE.portalGetObjectID(ptr);
            iteration = BaseAI.iteration;
    }

    boolean validify()
    {
        if(iteration == BaseAI.iteration) return true;
        for(int i = 0; i < BaseAI.portals.length; i++)
        {
          if(BaseAI.portals[i].ID == ID)
            {
                ptr = BaseAI.portals[i].ptr;
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
        return Client.INSTANCE.portalGetObjectID(ptr);
    }
    public int getX()
    {
        validify();
        return Client.INSTANCE.portalGetX(ptr);
    }
    public int getY()
    {
        validify();
        return Client.INSTANCE.portalGetY(ptr);
    }
    public int getZ()
    {
        validify();
        return Client.INSTANCE.portalGetZ(ptr);
    }
    public int getDirection()
    {
        validify();
        return Client.INSTANCE.portalGetDirection(ptr);
    }
    public int getFee()
    {
        validify();
        return Client.INSTANCE.portalGetFee(ptr);
    }
    public int getFeeIncr()
    {
        validify();
        return Client.INSTANCE.portalGetFeeIncr(ptr);
    }
    public float getFeeMultiplier()
    {
        validify();
        return Client.INSTANCE.portalGetFeeMultiplier(ptr);
    }
}

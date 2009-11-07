import com.sun.jna.Pointer;

///The attributes of a specific tile of the world.
class Terrain
{
    Pointer ptr;
    int ID;
    int iteration;
    public Terrain(Pointer p)
    {
            ptr = p;
            ID = Client.INSTANCE.terrainGetObjectID(ptr);
            iteration = BaseAI.iteration;
    }

    boolean validify()
    {
        if(iteration == BaseAI.iteration) return true;
        for(int i = 0; i < BaseAI.terrains.length; i++)
        {
          if(BaseAI.terrains[i].ID == ID)
            {
                ptr = BaseAI.terrains[i].ptr;
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
        return Client.INSTANCE.terrainGetObjectID(ptr);
    }
    public int getX()
    {
        validify();
        return Client.INSTANCE.terrainGetX(ptr);
    }
    public int getY()
    {
        validify();
        return Client.INSTANCE.terrainGetY(ptr);
    }
    public int getZ()
    {
        validify();
        return Client.INSTANCE.terrainGetZ(ptr);
    }
    public int getBlocksMove()
    {
        validify();
        return Client.INSTANCE.terrainGetBlocksMove(ptr);
    }
    public int getBlocksBuild()
    {
        validify();
        return Client.INSTANCE.terrainGetBlocksBuild(ptr);
    }
}

///The class implementing gameplay logic.
class AI extends BaseAI
{
  public String username()
  {
    return "Shell AI";
  }
  public String password()
  {
    return "password";
  }
  public boolean run()
  {
    for (Unit u : units) {
      UnitType ut = getTypeFromUnit(u);
      System.out.println("HERE'S THE UNIT TYPE: " + ut.getName());
    }
    for (Building b : buildings) {
      BuildingType bt = getTypeFromBuilding(b);
      System.out.println("HERE'S THE BUILDING TYPE: " + bt.getName());
    }

    return true;
  }

  public void init() {}
}

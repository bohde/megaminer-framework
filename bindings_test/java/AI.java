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
      if (ut.getName() == "Artist")
          System.out.println(artWorth(u.getLevel(), 0));
    }

    return true;
  }

  public void init() {}
}

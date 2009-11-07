///AI
import java.util.Random;
import java.lang.Math;
import java.lang.Integer;

class AI extends BaseAI
{
  public class Point {
    public Point() {
      this.x = 0;
      this.y = 0;
      this.z = 0;
    }
 
    public Point(int x1, int y1, int z1) {
      this.x = x1;
      this.y = y1;
      this.z = z1;
    }

    public int x;
    public int y;
    public int z;
  };

  static final String ENGINEER = "Engineer";
  static final String ARTIST = "Artist";
  static final String SPEARMAN = "Spearnam";
  static final String ARTILLERY = "Artillery";
  static final String CAVALRY = "Cavalry";
  static final String PIG = "Pig";
  static final String ANY_UNIT = "Any Unit";

  static final String SCHOOL = "School";
  static final String GALLERY = "Gallery";
  static final String FARM = "Farm";
  static final String BARRACKS = "Barracks";
  static final String BUNKER = "Bunker";
  static final String ANY_BUILDING = "Any Building";

  public String username() {
    return "Shell AI";
  }

  public String password() {
    return "password";
  }

  // Returns distance between two points
  public int distance(int x1, int y1, int z1, int x2, int y2, int z2) {
    if (z1 == z2)
      return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    else
      return Integer.MAX_VALUE;
  }

  // Gets the unit type of a unit, null if not found
  public UnitType getUnitType(Unit u) {
    int typeID = u.getUnitTypeID();
    for (UnitType t: unitTypes) {
      if (t.getObjectID() == typeID)
        return t;
    }
    return null;
  }

  // Gets the type of a building, null if not found
  public BuildingType getBuildingType(Building b) {
    int typeID = b.getBuildingTypeID();
    for (BuildingType t: buildingTypes) {
      if (t.getObjectID() == typeID)
        return t;
    }
    return null;  
  }

  // Returns the location of the closest enemy unit of the specified type
  // Returns null if there aren't any enemy units in the time period
  public Point closestEnemyUnit(String type, int x, int y, int z) {
    Point point = new Point();
    boolean found = false;
    int closest = Integer.MAX_VALUE;
    for (Unit u: units) {
      if (u.getOwnerID() != playerID()) {
        String enemyType = getUnitType(u).getName();
        if (enemyType == type || type == ANY_UNIT) {
          int dist = distance(x, y, z, u.getX(), u.getY(), u.getZ());
          if (dist < closest && z == u.getZ()) {
            closest = dist;
            found = true;
            point.x = u.getX();
            point.y = u.getY();
            point.z = u.getZ();
          }
        }
      }
    }

    if (found)
      return point;
    return null;
  }

  // Returns the location of the closest enemy biulding of the specified type  
  // Returns null if there arne't any enemy buildings in the time period
  // TODO: Use new building detection function
  public Point closestEnemyBuilding(String type, int x, int y, int z) {
    Point point = new Point();
    boolean found = false;
    int closest = Integer.MAX_VALUE;
    for (Building b: buildings) {
      if (b.getOwnerID() != playerID()) {
        String enemyType = getBuildingType(b).getName();
        if (enemyType == type || type == ANY_BUILDING) {
          int dist = distance(x, y, z, b.getX(), b.getY(), b.getZ());
          if (dist < closest && z == b.getZ()) {
            closest = dist;
            found = true;
            point.x = b.getX();
            point.y = b.getY();
            point.z = b.getZ();
          }
        }
      }
    }

    if (found)
      return point;
    return null;
  }

  // Returns the location of the closest enemy building OR unit
  // Null if none exist
  public Point closestEnemyObject(int x, int y, int z) {
    Point p1 = new Point();
    Point p2 = new Point();
    int d1 = Integer.MAX_VALUE, d2 = Integer.MAX_VALUE;

    p1 = closestEnemyUnit(ANY_UNIT, x, y, z);
    if (p1 != null)
      d1 = distance(x, y, z, p1.x, p1.y, p1.z);

    p2 = closestEnemyBuilding(ANY_BUILDING, x, y, z);
    if (p2 != null)
      d2 = distance(x, y, z, p2.x, p2.y, p2.z);

    if (p1 == null && p2 == null)
      return null;
    else if (p1 != null && p2 == null)
      return p1;
    else if (p1 == null && p2 != null)
      return p2;
    else
      return (d1 < d2? p1 : p2);
  }

  // Returns point that unit should move to toward goal square
  // Returns null if the points aren't in the same time period
  // TODO: Go around blocking terrain, use new building detection functions
  public Point moveToward(int curr_x, int curr_y, int curr_z, int x, int y, int z) {
    if (curr_z != z)
      return null;

    Point point = new Point();
    int diff_x = curr_x - x;
    int diff_y = curr_y - y;

    if (Math.abs(diff_x) > Math.abs(diff_y)) {
      if (diff_x > 0 {
        point.x = curr_x - 1;
        point.y = curr_y;
      }
      else {
        point.x = curr_x + 1;
        point.y = curr_y;
      }
    }
    else {
      if (diff_y > 0) {
        point.y = curr_y - 1;
        point.x = curr_x;
      }
      else {
        point.y = curr_y + 1;
        point.x = curr_x;
      }
    }

    return point;
  }

  // If move is true, then checks if a move can be made to the supplied point
  // If move is false, check if a build can be made at the supplied point
  public boolean canMoveOrBuild(boolean move, int x, int y, int z) {
    Point p = new Point(x, y, z);
    for (Terrain t: terrains) {
      Point temp = new Point(t.getX(), t.getY(), t.getZ());
      if (move && temp == p && t.getBlockMove())
        return false;
      else if (!move && temp == p && t.getBlockBuild())
        return false;
    }

    Building b = getBuilding(p.x, p.y, p.z);
    if (b != null && b.getOwnerID() != playerID())
      return false;

    for (Unit u: units) {
      Point temp = new Point(u.getX(), u.getY(), u.getZ());
      if (temp == p && u.getOwnerID() != playerID())
        return false;
    }

    if (!move) {
      for (Portal por : portals) {
        Point temp = new Point(por.getX(), por.getY(), por.getZ());
        if (p == temp)
          return false;
      }
    }

    return true;
  }

  // Returns true if a building can be built at the supplied point
  public boolean canBuild(int x, int y, int z) {
    return canMoveOrBuild(false, x, y, z);
  }

  // Returns true if a unit can move to the supplied point
  public boolean canMove(int x, int y, int z) {
    return canMoveOrBuild(true, x, y, z);
  }

  // Returns the building that contains the provided point
  // Null otherwise
  public Building getBuilding(int x, int y, int z) {
    Point p = new Point(x, y, z);
    for (Building b: buildings) {
      BuildingType t = getBuildingType(b);
      for (int i = 0; i < t.getWidth(); i++) {
        for (int j = 0; j < t.getHeight(); j++) {
          Point temp = new Point(b.getX() + i, b.getY() + j, b.getZ());
          if (p == temp)
            return b;
        } 
      }
    }
    return null;
  }

  // Returns the point of an adjacent enemy object, null if nothing is adjacent
  public Point isAdjacent(int x, int y, int z) {
    int e_x, e_y, e_z;
    for (Building b: buildings) {
      e_x = b.getX();
      e_y = b.getY();
      e_z = b.getZ();
      if (e_z == z && (Math.abs(x - e_x) == 1 || Math.abs(y - e_y) == 1))
        return new Point(e_x, e_y, e_z);        
    }

    for (Unit u: units) {
      e_x = u.getX();
      e_y = u.getY();
      e_z = u.getZ();
      if (e_z == z && (Math.abs(x - e_x) == 1 || Math.abs(y - e_y) == 1))
        return new Point(e_x, e_y, e_z);
    }

    return null;    
  }

  // Returns true if the given unit can attack this turn
  public boolean canAttack(Unit u, UnitType t) {
    if (t.getAttackCost <= u.getMoves() && u.getActions() >= 1)
      return true;
    return false;
  }

  // Drives the AI code
  public boolean run() {
    for (Unit u : units) {
      if (u.getOwnerID() == playerID()) {
        UnitType type = getUnitType(u);
        Point point = new Point();
        if (type.getName() == ENGINEER) {
          // Build or dance
        }
        else if (type.getName() == ARTIST) {
          // Paint or move
        }
        else {
          Point goal = closestEnemyObject(u.getX(), u.getY(), y.getZ());
          // If there is an ememy object in the time period
          if (goal != null) {
            while (type.getMoves() > 0) {
              Point adj = isAdjacent(u.getX(), u.getY(), u.getZ());
              // If not adjacent to any enemy units
              if (adj == null) {
                Point moveTo = moveToward(u.getX(), u.getY(), u.getZ(), goal.x, goal.y, goal.z);
                u.move(moveTo.x, moveTo.y);
              }
              // If adjacent and able to attack
              else if (canAttack(u, type) {
                u.attack(adj.x, adj.y);
              }
              // If adjacent and unable to attack
              else {
                // TODO: Move away
                break;
              }
            }
          }
          // TODO: Eventually move to a new time period
          else {
            // Add code to move to another time period here
          }  
        }
      }
    }    
    return true;
  }

  public void init() {}
}

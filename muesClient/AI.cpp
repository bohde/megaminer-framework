#include "AI.h"
#include <math.h>

const char* AI::username()
{
  return "Shell AI";
}

const char* AI::password()
{
  return "password";
}

void AI::init(){}

bool AI::run()
{
  for (int i = 0; i < unitTypes.size(); i++)
  {
    cout << i << " : " << unitTypes[i].name() << endl;
  }

  printMap(1);
  cout << "Starting turn " << turnNumber() << endl;
  cout << "Player0Gold0 " << player0Gold0() << endl;
  cout << "Buildings on map : " << buildings.size() << endl;
  cout << "Units on map : " << units.size() << endl;
  UnitType myType;
  int count = 0;

  for (int i = 0; i < 6; i++)
  {
    goldSpent[i] = 0;
  }

  for (int i = 0; i<portals.size(); i++)
  {
    portalFees[i] = portals[i].fee();
  }

  for (int i = 0; i < buildings.size(); i++)
  {
    if (rand()%100 < 2 && (!buildings[i].complete() || 
        buildings[i].inTraining() != -1) && 
        buildings[i].ownerID() == playerID())
    {
      buildings[i].cancel();
    }

    if (buildings[i].ownerID() == playerID())
    {
      trainUnits(buildings[i]);
    }
  }
  for (int i = 0; i < units.size(); i++)
  {
    if (units[i].ownerID() == playerID())
    {
      myType = getType(units[i]);
//      cout << "("<< units[i].objectID() << ")"
//                 << myType.name() << " : (" << units[i].x() << ", " 
//                 << units[i].y() << ") " << units[i].ownerID()<< endl;
      if (strcmp(myType.name(),"Artist")==0)
      {
        doArtist(units[i]);
      }
      else if (strcmp(myType.name(),"Engineer")==0)
      {
        doEngineer(units[i]);
      }
      else if (strcmp(myType.name(), "Pig") == 0)
      {
        randomWalk(units[i], units[i].moves());
      }
      else
      {
        doCombatUnit(units[i]);
        count += 1;
      }
    }
  }
  cout << "Combat Units : " << count << endl;
  return true;
}

void AI::trainUnits(Building& b)
{
  int newTypeIndex;
  int tries = 0;
  //Focus combat training in present
  int chance = 10 + 30*b.z();
    
  do
  {
    newTypeIndex = rand()%unitTypes.size();
    tries++;
  } while (tries < 6 &&
            unitTypes[newTypeIndex].trainerID()!=getType(b).objectID());

  if ( strcmp(unitTypes[newTypeIndex].name(), "Engineer") == 0)
  {
    chance = 20;
    if (getGold(playerID(), b.z()) < END_THRIFT && 
        perHasUnitAtLeastLvl("Engineer", b.z(), b.level()))
    {
      chance = 0;
    }
  }
  else if (strcmp(unitTypes[newTypeIndex].name(), "Pig") == 0)
  {
    chance = 1;
  }
  else if (strcmp(unitTypes[newTypeIndex].name(), "Artist") == 0)
  {
    chance = 20;
  }

  if (expectedHunger(b.z()) > -5)
  {
    chance = 0;
  }


  if (unitTypes[newTypeIndex].trainerID()==getType(b).objectID()
       && rand()% 100 < chance && b.complete() && b.inTraining() == -1
       && getGold(playerID(), b.z()) 
          > effPrice(unitTypes[newTypeIndex], b.level()))
  {
    b.train(unitTypes[newTypeIndex]);
    spendGold(playerID(), b.z(), effPrice(unitTypes[newTypeIndex], b.level()));
  }
}

void AI::doArtist(Unit& u)
{
  Building* gallery = getBuilding(u.x(), u.y(), u.z());
  BuildingType bt;

  if (gallery == NULL)
  {
    randomWalk(u, u.moves());
  }
  else
  {
    bt = getType(*gallery);
    if (strcmp(bt.name(), "Gallery")==0 && u.actions() > 0)
    {
      u.paint(u.x(), u.y());
    }
    else
    {
      randomWalk(u, u.moves());
    }
  }
}

//If I already have a unit of this type of my level or higher in this
// time period, return true
bool AI::perHasUnitAtLeastLvl(const char typeName[100], int z, int level)
{
  bool hasOne = false;

  for (int i = 0; i < units.size(); i++)
  {
    if (units[i].ownerID() == playerID()
        && strcmp(getType(units[i]).name(), typeName) == 0
        && units[i].level() >= level
        && units[i].z() == z)
    {
      hasOne = true;
      break;
    }
  }

  return hasOne;
}


//If I already have a building of this type of my level or higher in this
// time period, return true
bool AI::perHasBuildAtLeastLvl(const char typeName[100], int z, int level)
{
  
  bool hasOne = false;

  for (int i = 0; i < buildings.size(); i++)
  {
    if (buildings[i].ownerID() == playerID()
        && strcmp(getType(buildings[i]).name(), typeName) == 0
        && buildings[i].level() >= level
        && buildings[i].z() == z
        && buildings[i].complete() == 1)
    {
      hasOne = true;
      break;
    }
  }

  return hasOne;
}

void AI::doEngineer(Unit& u)
{
  int typeIndex = rand()%buildingTypes.size();
  BuildingType bt = buildingTypes[typeIndex];
  int chance = 100;

  bool hasBarracks = perHasBuildAtLeastLvl("Barracks", u.z(), u.level());
  bool hasGallery = perHasBuildAtLeastLvl("Gallery", u.z(), u.level());
  bool hasSchool = perHasBuildAtLeastLvl("School", u.z(), u.level());
  
  while (getGold(playerID(), u.z()) < END_THRIFT
      && ((hasBarracks && strcmp(bt.name(), "Barracks")==0)
       ||(hasGallery && strcmp(bt.name(), "Gallery")==0)
       ||(hasSchool && strcmp(bt.name(), "School") == 0))) 
  {
    typeIndex = rand()%buildingTypes.size();
    bt = buildingTypes[typeIndex];
  }


  if (strcmp(buildingTypes[typeIndex].name(),"Barracks") == 0)
  {
    chance = 100;
  }
  else if (strcmp(buildingTypes[typeIndex].name(),"Gallery") == 0)
  {
    chance = 10;
  }
  else if (strcmp(buildingTypes[typeIndex].name(),"School") == 0)
  {
    chance = 5;
  }
  else if (strcmp(buildingTypes[typeIndex].name(),"Farm") == 0)
  {
    chance = 100;
  }
  else if (strcmp(buildingTypes[typeIndex].name(),"Bunker") == 0)
  {
    chance = 5;
  }

  //Focus construction in the past
  chance = chance / (u.z() + 1);
  
  Building* thisBuilding = getBuilding(u.x(), u.y(), u.z());
  
  if (areaClear(u.x(), u.y(), u.z(), typeIndex) 
      && getGold(playerID(), u.z()) 
        > effPrice(buildingTypes[typeIndex], u.level())
      && rand()%100 < chance)
  {
    u.build(u.x(), u.y(), buildingTypes[typeIndex]);
    spendGold(playerID(), u.z(), effPrice(buildingTypes[typeIndex], u.level()));
  }
  else if (thisBuilding == NULL)
  {
    randomWalk(u, u.moves());
  }
  else if (thisBuilding->complete() == 0)
  {
    BuildingType targetType = getType(*thisBuilding);
    u.build(u.x(), u.y(), targetType);
  }
  else
  {
    randomWalk(u, u.moves());
  }
}

/*
int AI::effPrice(BuildingType bt, int level)
{
  return static_cast<int>(bt.price() * pow(bt.priceExp(), level));
}

int AI::effPrice(UnitType ut, int level)
{
  return static_cast<int>(ut.price() * pow(ut.priceExp(), level));
}

*/


bool AI::areaClear(int x, int y, int z, int typeIndex)
{
  for (int j = x; j < x + buildingTypes[typeIndex].width(); j++)
  {
    for (int k = y; k < y + buildingTypes[typeIndex].height(); k++)
    {
      if (!canBuild(j, k, z))
      {
        return false;
      }
    }
  }
  return true;
}


//Returns true if I can build on this square
/*
bool AI::isClear(int x, int y, int z)
{
  if (abs(x) > 10 || abs(y) > 10)
    return false;
  for (int i = 0; i < portals.size(); i++)
  {
    if (portals[i].x() == x && portals[i].y() == y &&
        portals[i].z() == z)
      return false;
  }
  for (int i = 0; i < terrains.size(); i++)
  {
    if (terrains[i].x() == x && terrains[i].y() == y && 
        terrains[i].z() == z)
       // && terrains[i].blockbuild() == true)
      return false;
  }
  for (int i = 0; i < units.size(); i++)
  {
    if (units[i].x() == x && units[i].y() == y && 
       units[i].z() == z && units[i].ownerID() != playerID())
      return false;
  }
  for (int i = 0; i < buildings.size(); i++)
  {
    BuildingType bt = getType(buildings[i]);
    if (z == buildings[i].z() && 
        x >= buildings[i].x() && x < buildings[i].x() + bt.width() &&
        y >= buildings[i].y() && y < buildings[i].y() + bt.height())
      return false;
  }
  return true;
}
*/

/*
bool AI::canWalk(int x, int y, int z)
{
  for (int i = 0; i < terrains.size(); i++)
  {
    if (terrains[i].x() == x && terrains[i].y() == y &&
        terrains[i].z() == z)
       // && terrains[i].blockbuild() == true)
      return false;
  }
  for (int i = 0; i < units.size(); i++)
  {
    if (units[i].x() == x && units[i].y() == y &&
       units[i].z() == z && units[i].ownerID() != playerID())
      return false;
  }
  for (int i = 0; i < buildings.size(); i++)
  {
    BuildingType bt = getType(buildings[i]);
    if (z == buildings[i].z() &&
        x >= buildings[i].x() && x < buildings[i].x() + bt.width() &&
        y >= buildings[i].y() && y < buildings[i].y() + bt.height()
        && buildings[i].ownerID() != playerID())
      return false;
  }
  return true;
}
*/

Building* AI::getBuilding(int x, int y, int z)
{
  for (int i = 0; i < buildings.size(); i++)
  {
    BuildingType bt = getType(buildings[i]);
    if (x >= buildings[i].x() && x < buildings[i].x() + bt.width() &&
        y >= buildings[i].y() && y < buildings[i].y() + bt.height() &&
        z == buildings[i].z())
      return &buildings[i];
  }
  return NULL;
}

void AI::doCombatUnit(Unit& u)
{
  int remainingMoves = u.moves();
  int remainingActions = u.actions();

  for (int i = 0; i < u.actions(); i++)
  {
    //attack any units in your range
    Unit* target = anyInRange(u);
    if (target != NULL)
    {
      u.attack(target->x(), target->y());
      remainingMoves -= getType(u).attackcost();
      remainingActions -= 1;
    }
  }
    
  for (int i = 0; i < remainingActions; i++)
  {
    //attack any buildings in your range
    Building* targetB = anyBuildInRange(u);
    if (targetB != NULL)
    {
      u.attack(targetB->x(), targetB->y());
      remainingMoves -= getType(u).attackcost();
    }
  }
  randomWalk(u, remainingMoves);
}

//Returns an enemy in attack range
Unit* AI::anyInRange(Unit& u)
{
  UnitType ut = getType(u);
  for (int i = 0; i < units.size(); i++)
  {
    if (units[i].ownerID() != playerID() 
    &&    distance(u, units[i]) <= ut.maxrange() &&
        distance(u, units[i]) >= ut.minrange())
    {
      return &units[i];
    }
  }
  return NULL;
}

Building* AI::anyBuildInRange(Unit& u)
{
  UnitType ut = getType(u);
  for (int i = 0; i < buildings.size(); i++)
  {
    if (buildings[i].ownerID() != playerID()
    &&    distance(u, buildings[i]) <= ut.maxrange() &&
        distance(u, buildings[i]) >= ut.minrange())
    {
      return &buildings[i];
    }
  }
  return NULL;

}

void AI::randomWalk(Unit& u, int moves)
{
  int curX = u.x(), curY = u.y(), curZ = u.z();
  Portal* myPortal = NULL;
  for (int i = 0; i < moves; i++)
  {
    myPortal = NULL;
    int yOffset = rand()%3 -1;
    int xOffset = (abs(yOffset) - 1) * (2*(rand()%2) - 1);
    
    //Drift towards enemy
    if ( ((playerID() == 1) == (xOffset + yOffset < 0))
         && rand() % 10 == 0)
    {
      xOffset *= -1;
      yOffset *= -1;
    }

    if (abs(xOffset + yOffset) > 0 && 
        abs(xOffset+curX) <= 10 &&
        abs(yOffset+curY) <= 10 && 
        canMove(xOffset+curX,yOffset+curY, curZ))
    {
      u.move(curX+xOffset, curY+yOffset);
      curX += xOffset;
      curY += yOffset;
    }
    myPortal = getPortalAt(curX, curY, curZ);
    if (myPortal != NULL)
    {
      if ((expectedHunger(curZ) > 5+expectedHunger(curZ + myPortal->direction())
          && getGold(playerID(), curZ)>getPortalFee(*myPortal))
         || (strcmp(getType(u).name(), "Engineer") == 0
             && !perHasUnitAtLeastLvl("Engineer",u.z()+myPortal->direction(),u.level())))
      {
        u.warp();
        spendGold(playerID(), curZ, getPortalFee(*myPortal));
        portalFees[getPortalIndex(*myPortal)] += 10;
        curZ += myPortal->direction();
      }
    }
  }
  return;
}

Portal* AI::getPortalAt(int x, int y, int z)
{
  for (int i = 0; i < portals.size(); i++)
  {
    if (portals[i].x() == x && portals[i].y() == y && portals[i].z() == z)
      return &portals[i];
  }
  return NULL;
}

/*
UnitType AI::getType(Unit& u)
{
  for (int i = 0; i < unitTypes.size(); i++)
  {
    if (unitTypes[i].objectID() == u.unitTypeID())
    {
      return unitTypes[i];
    }
  }
  return NULL;
}
*/

/*
BuildingType AI::getType(Building& b)
{
  for (int i = 0; i < buildingTypes.size(); i++)
  {
    if (buildingTypes[i].objectID() == b.buildingTypeID())
    {
      return buildingTypes[i];
    }
  }
  return NULL;
}
*/


/*
int AI::distance(int x1, int y1, int z1, int x2, int y2, int z2)
{
  if (z1 == z2)
    return abs(x1-x2)+abs(y1-y2);
  else
    return 9999;
}

int AI::distance(Unit& a, Unit& b)
{
  return distance(a.x(), a.y(), a.z(), b.x(), b.y(), b.z());
}

int AI::distance(Unit& a, Portal& b)
{
  return distance(a.x(), a.y(), a.z(), b.x(), b.y(), b.z());
}

int AI::distance(Unit& a, Building& b)
{
  return distance(a.x(), a.y(), a.z(), b.x(), b.y(), b.z());
}

*/

int AI::getGold(int playerNum, int z)
{
  int gold = BaseAI::getGold(playerNum, z);
  return gold - goldSpent[3*playerNum+z];
}

//Track gold expenses this turn
void AI::spendGold(int playerNum, int z, int gold)
{
  goldSpent[3*playerNum+z] += gold;
}

int AI::getPortalIndex(Portal p)
{
  int index = 0;
  for (int i = 0; i < portals.size(); i++)
  {
    if (p.objectID() == portals[i].objectID())
    {
      index = i;
    }
  }
  return index;
}

int AI::getPortalFee(Portal p)
{
  return portalFees[getPortalIndex(p)];
}

//Amount of food produced by this building
int AI::effFood(Building b)
{
  BuildingType bt = getType(b);
  return BaseAI::effFood(bt, b.level());
}


int AI::expectedHunger(int z)
{
  int hunger = 0;
  for (int i = 0; i < buildings.size(); i++)
  {
    if (buildings[i].z() == z && buildings[i].ownerID() == playerID()
        && buildings[i].complete() == 1)
    {
      hunger -= effFood(buildings[i]);
    }
  }

  for (int i = 0; i < units.size(); i++)
  {
    if (units[i].z() == z && units[i].ownerID() == playerID())
    {
      UnitType ut = getType(units[i]);
      hunger += ut.hunger();
    }
  }
  return hunger;
}

BuildingType AI::getBuildingType(const char typeName[500])
{
  for (int i = 0; i < buildingTypes.size(); i++)
  {
    if (strcmp(buildingTypes[i].name(), typeName)==0)
    {
      return buildingTypes[i];
    }
  }
}

/*
void AI::plotPoint(char * output, int x, int y, int z, 
                   char label, int fg, int bg)
{
  int index = (x + 10) + ((-1*y) + 10) *  + z 
}
*/

void AI::printMap(int z)
{
  cout << "=====================" << endl;

  char output[463];
  int c;
  output[462] = '\0';

  //newlines and empty
  for (c = 0; c < 462; c+=1)
  {
    output[c] = ' ';
    if (c%22==21)
    {
      output[c] = '\n';
    }
  }

  for (int i = 0; i < portals.size(); i++)
  {
    if (portals[i].z() == z)
    {
      c = portals[i].x() + 10 + (-1*portals[i].y() + 10) * 22;
      output[c] = 'P';
    }
  }

  for (int i = 0; i < terrains.size(); i++)
  {
    if (terrains[i].z() == z)
    {
      c = terrains[i].x() + 10 + (-1*terrains[i].y() + 10) * 22;
      output[c] = 'T';
    }
  }


  for (int i = 0; i < buildings.size(); i++)
  {
    if (buildings[i].z() == z)
    {
      for (int x = buildings[i].x(); x < buildings[i].x() + 2; x++)
      {
        for (int y = buildings[i].y(); y < buildings[i].y() + 2; y++)
        {
          c = x + 10 + (-1*y + 10) * 22;
          if (buildings[i].complete() == 1)
          {
            output[c] = 'B';
          }
          else
          {
            output[c] = 'b';
          }
          output[c] = '0' + buildings[i].level();
        }
      }
    }
  }
  for (int i = 0; i < units.size(); i++)
  {
    if (units[i].z() == z)
    {
      c = units[i].x() + 10 + (-1*units[i].y() + 10) * 22;
      //output[c] = '0' + units[i].unitTypeID();
      output[c] = '0' + units[i].level();
    }
  }
  cout << output;
}

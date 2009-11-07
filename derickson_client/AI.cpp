#include "AI.h"
#include<cstdlib>
#include<ctime>

const char* AI::username()
{
  return "Shell AI";
}

const char* AI::password()
{
  return "password";
}

void AI::init(){}

// RIght now, this client just randomly moves stuff
bool AI::run()
{
  const int MAX_X = 10;
  const int MAX_Y = 10;
  srand(time(NULL));

  for (unsigned int i = 0; i < units.size(); i++) {
    int dir = rand() % 4;
    // Move up
    if (dir == 0 && units[i].y() < MAX_Y)
      units[i].move(units[i].x(), units[i].y() + 1);
    // Move down
    else if (dir == 1 && units[i].y() > -MAX_Y)
      units[i].move(units[i].x(), units[i].y() - 1);
    // Move right
    else if (dir == 2 && units[i].x() < MAX_X)
      units[i].move(units[i].x() + 1, units[i].y());
    // Move left
    else if (dir == 3 && units[i].x() > -MAX_X)
      units[i].move(units[i].x() - 1, units[i].y());
  }
  return true;
}

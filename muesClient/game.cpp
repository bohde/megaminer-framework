//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#pragma warning(disable : 4996)

#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>

#include "game.h"
#include "network.h"
#include "structures.h"

#include "sexp/sexp.h"
#include "sexp/sexp_ops.h"

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

#ifdef WIN32
//Doh, namespace collision.
namespace Windows
{
    #include <Windows.h>
};
#else
#include <unistd.h>
#endif

using namespace std;

static int player0Gold0 = 0;
static int player0Gold1 = 0;
static int player0Gold2 = 0;
static int player1Gold0 = 0;
static int player1Gold1 = 0;
static int player1Gold2 = 0;
static int playerID = 0;
static int turnNumber = 0;


static _Building* Buildings = NULL;
static int BuildingCount = 0;

static _BuildingType* BuildingTypes = NULL;
static int BuildingTypeCount = 0;

static _Portal* Portals = NULL;
static int PortalCount = 0;

static _Terrain* Terrains = NULL;
static int TerrainCount = 0;

static _Unit* Units = NULL;
static int UnitCount = 0;

static _UnitType* UnitTypes = NULL;
static int UnitTypeCount = 0;


static int socket;

//These two are needed to save the login credentials for repeated internal use
static char* last_username = NULL;
static char* last_password = NULL;


DLLEXPORT bool serverLogin(int s, const char* username, const char* password)
{
  socket = s;
  
  if(!last_username)
    last_username = strdup(username);
  if(!last_password)
    last_password = strdup(password);

  string expr = "(login \"";
  expr += username;
  expr += "\" \"";
  expr += password;
  expr +="\")";

  send_string(socket, expr.c_str());

  sexp_t* expression;

  expression = extract_sexpr(rec_string(socket));
  expression = expression->list;
  if(expression->val == NULL || strcmp(expression->val, "login-accepted") != 0)
  {
    cerr << "Unable to login to server" << endl;
    return false;
  }
  return true;
}

DLLEXPORT int createGame()
{
  sexp_t* expression;
  int gameNum;

  send_string(socket, "(start-game)");
  expression = extract_sexpr(rec_string(socket));
  expression = expression->list->next;
  gameNum = atoi(expression->val);
  
  std::cout << "Creating game " << gameNum << endl;
  
  expression = expression->next->list->next->next;

  socket = open_server_connection(expression->val, "19001");
  serverLogin(socket, last_username, last_password);

  stringstream expr;
  expr << "(create-game " << gameNum << ")";
  send_string(socket, expr.str().c_str());
  
  expr.str("");
  expr << "(join-game " << gameNum << ")";
  send_string(socket, expr.str().c_str());
  
  return socket;

}

DLLEXPORT int joinGame(int gameNum)
{
  sexp_t* expression;
  stringstream expr;
  
  //get the server of the game
  expr << "(join-game " << gameNum << ")";
  send_string(socket, expr.str().c_str());
  
  //redirect
  expression = extract_sexpr(rec_string(socket));
  expression = expression->list->next->next;
  
  socket = open_server_connection(expression->val, "19001");
  serverLogin(socket, last_username, last_password);
  
  //join and start the game
  send_string(socket, expr.str().c_str());
  send_string(socket, "(game-start)");
  
  return socket;
}

DLLEXPORT void endTurn()
{
  send_string(socket, "(end-turn)");
}

DLLEXPORT void getStatus()
{
  send_string(socket, "(game-status)");
}


DLLEXPORT bool buildingTrain(_Building* object, _UnitType* unit)
{
  stringstream expr;
  expr << "(game-train " << object->objectID
      << " " << unit->objectID
       << ")";
  send_string(socket, expr.str().c_str());
  return true;
}

DLLEXPORT bool buildingCancel(_Building* object)
{
  stringstream expr;
  expr << "(game-cancel " << object->objectID
       << ")";
  send_string(socket, expr.str().c_str());
  return true;
}

DLLEXPORT bool unitAttack(_Unit* object, int x, int y)
{
  stringstream expr;
  expr << "(game-attack " << object->objectID
       << " " << x
       << " " << y
       << ")";
  send_string(socket, expr.str().c_str());
  return true;
}

DLLEXPORT bool unitBuild(_Unit* object, int x, int y, _BuildingType* type)
{
  stringstream expr;
  expr << "(game-build " << object->objectID
       << " " << x
       << " " << y
      << " " << type->objectID
       << ")";
  send_string(socket, expr.str().c_str());
  return true;
}

DLLEXPORT bool unitPaint(_Unit* object, int x, int y)
{
  stringstream expr;
  expr << "(game-paint " << object->objectID
       << " " << x
       << " " << y
       << ")";
  send_string(socket, expr.str().c_str());
  return true;
}

DLLEXPORT bool unitMove(_Unit* object, int x, int y)
{
  stringstream expr;
  expr << "(game-move " << object->objectID
       << " " << x
       << " " << y
       << ")";
  send_string(socket, expr.str().c_str());
  return true;
}

DLLEXPORT bool unitWarp(_Unit* object)
{
  stringstream expr;
  expr << "(game-warp " << object->objectID
       << ")";
  send_string(socket, expr.str().c_str());
  return true;
}

//Utility functions for parsing data
void parseBuilding(_Building* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;
  
  object->objectID = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;
  object->z = atoi(sub->val);
  sub = sub->next;
  object->hp = atoi(sub->val);
  sub = sub->next;
  object->level = atoi(sub->val);
  sub = sub->next;
  object->buildingTypeID = atoi(sub->val);
  sub = sub->next;
  object->ownerID = atoi(sub->val);
  sub = sub->next;
  object->inTraining = atoi(sub->val);
  sub = sub->next;
  object->progress = atoi(sub->val);
  sub = sub->next;
  object->linked = atoi(sub->val);
  sub = sub->next;
  object->complete = atoi(sub->val);
  sub = sub->next;
  
}
void parseBuildingType(_BuildingType* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;
  
  object->objectID = atoi(sub->val);
  sub = sub->next;
  object->name = new char[strlen(sub->val)+1];
  strncpy(object->name, sub->val, strlen(sub->val));
  object->name[strlen(sub->val)] = 0;
  sub = sub->next;
  object->price = atoi(sub->val);
  sub = sub->next;
  object->food = atoi(sub->val);
  sub = sub->next;
  object->pastBuildTime = atoi(sub->val);
  sub = sub->next;
  object->presentBuildTime = atoi(sub->val);
  sub = sub->next;
  object->futureBuildTime = atoi(sub->val);
  sub = sub->next;
  object->hp = atoi(sub->val);
  sub = sub->next;
  object->armor = atoi(sub->val);
  sub = sub->next;
  object->builderID = atoi(sub->val);
  sub = sub->next;
  object->allowPaint = atoi(sub->val);
  sub = sub->next;
  object->width = atoi(sub->val);
  sub = sub->next;
  object->height = atoi(sub->val);
  sub = sub->next;
  object->spawnX = atoi(sub->val);
  sub = sub->next;
  object->spawnY = atoi(sub->val);
  sub = sub->next;
  object->armorExp = atof(sub->val);
  sub = sub->next;
  object->hpExp = atof(sub->val);
  sub = sub->next;
  object->priceExp = atof(sub->val);
  sub = sub->next;
  object->foodExp = atof(sub->val);
  sub = sub->next;
  
}
void parsePortal(_Portal* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;
  
  object->objectID = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;
  object->z = atoi(sub->val);
  sub = sub->next;
  object->direction = atoi(sub->val);
  sub = sub->next;
  object->fee = atoi(sub->val);
  sub = sub->next;
  
}
void parseTerrain(_Terrain* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;
  
  object->objectID = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;
  object->z = atoi(sub->val);
  sub = sub->next;
  object->blockmove = atoi(sub->val);
  sub = sub->next;
  object->blockbuild = atoi(sub->val);
  sub = sub->next;
  
}
void parseUnit(_Unit* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;
  
  object->objectID = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;
  object->z = atoi(sub->val);
  sub = sub->next;
  object->hp = atoi(sub->val);
  sub = sub->next;
  object->level = atoi(sub->val);
  sub = sub->next;
  object->unitTypeID = atoi(sub->val);
  sub = sub->next;
  object->ownerID = atoi(sub->val);
  sub = sub->next;
  object->actions = atoi(sub->val);
  sub = sub->next;
  object->moves = atoi(sub->val);
  sub = sub->next;
  
}
void parseUnitType(_UnitType* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;
  
  object->objectID = atoi(sub->val);
  sub = sub->next;
  object->name = new char[strlen(sub->val)+1];
  strncpy(object->name, sub->val, strlen(sub->val));
  object->name[strlen(sub->val)] = 0;
  sub = sub->next;
  object->price = atoi(sub->val);
  sub = sub->next;
  object->hunger = atoi(sub->val);
  sub = sub->next;
  object->traintime = atoi(sub->val);
  sub = sub->next;
  object->hp = atoi(sub->val);
  sub = sub->next;
  object->armor = atoi(sub->val);
  sub = sub->next;
  object->moves = atoi(sub->val);
  sub = sub->next;
  object->actions = atoi(sub->val);
  sub = sub->next;
  object->attackcost = atoi(sub->val);
  sub = sub->next;
  object->damage = atoi(sub->val);
  sub = sub->next;
  object->minrange = atoi(sub->val);
  sub = sub->next;
  object->maxrange = atoi(sub->val);
  sub = sub->next;
  object->trainerID = atoi(sub->val);
  sub = sub->next;
  object->canpaint = atoi(sub->val);
  sub = sub->next;
  object->armorExp = atof(sub->val);
  sub = sub->next;
  object->hpExp = atof(sub->val);
  sub = sub->next;
  object->priceExp = atof(sub->val);
  sub = sub->next;
  object->damageExp = atof(sub->val);
  sub = sub->next;
  object->paintBase = atoi(sub->val);
  sub = sub->next;
  object->paintLinear = atoi(sub->val);
  sub = sub->next;
  
}

DLLEXPORT int networkLoop(int socket)
{
  while(true)
  {
    sexp_t* expression, *sub, *subsub;
    expression = extract_sexpr(rec_string(socket));
    expression = expression->list;
    if(expression->val != NULL && strcmp(expression->val, "game-over") == 0)
    {
      return 0;
    }
    else if(expression->val != NULL && strcmp(expression->val, "log") == 0)
    {
      ofstream out;
      char filename[100];
      expression = expression->next;
      strcpy(filename, expression->val);
      strcat(filename, ".gamelog");
      expression = expression->next;
      out.open(filename);
      if (out.good())
        out.write(expression->val, strlen(expression->val));
      else
        cerr << "Error : Could not create log." << endl;
      out.close();
      return 0;
    }
    else if(expression->val != NULL && strcmp(expression->val, "game-accepted")==0)
    {
      char gameID[30];

      expression = expression->next;
      strcpy(gameID, expression->val);
      cout << "Created game " << gameID << endl;
    }
    else if(expression->val != NULL && strstr(expression->val, "denied"))
    {
      cout << expression->val << endl;
      cout << expression->next->val << endl;
    }
    else if(expression->val != NULL && strcmp(expression->val, "ident") == 0)
    {
      expression = expression->next->next->next;
      playerID = atoi(expression->val);
    }
    else if(expression->val != NULL && strcmp(expression->val, "status") == 0)
    {
      while(expression->next != NULL)
      {
        expression = expression->next;
        sub = expression->list;
        if(string(sub->val) == "game")
        {
          sub = sub->next;
          turnNumber = atoi(sub->val);
          sub = sub->next;
          
          subsub = sub->list;
          player0Gold0 = atoi(subsub->val);
          subsub = subsub->next;
          player0Gold1 = atoi(subsub->val);
          subsub = subsub->next;
          player0Gold2 = atoi(subsub->val);
          sub = sub->next;
          
          subsub = sub->list;
          player1Gold0 = atoi(subsub->val);
          subsub = subsub->next;
          player1Gold1 = atoi(subsub->val);
          subsub = subsub->next;
          player1Gold2 = atoi(subsub->val);
        }
        else if(string(sub->val) == "Building")
        {
          for(int i = 0; i < BuildingCount; i++)
          {
          }
          delete[] Buildings;
          BuildingCount =  sexp_list_length(expression)-1; //-1 for the header
          Buildings = new _Building[BuildingCount];
          for(int i = 0; i < BuildingCount; i++)
          {
            sub = sub->next;
            parseBuilding(Buildings+i, sub);
          }
        }
        else if(string(sub->val) == "BuildingType")
        {
          for(int i = 0; i < BuildingTypeCount; i++)
          {
            delete[] BuildingTypes[i].name;
          }
          delete[] BuildingTypes;
          BuildingTypeCount =  sexp_list_length(expression)-1; //-1 for the header
          BuildingTypes = new _BuildingType[BuildingTypeCount];
          for(int i = 0; i < BuildingTypeCount; i++)
          {
            sub = sub->next;
            parseBuildingType(BuildingTypes+i, sub);
          }
        }
        else if(string(sub->val) == "Portal")
        {
          for(int i = 0; i < PortalCount; i++)
          {
          }
          delete[] Portals;
          PortalCount =  sexp_list_length(expression)-1; //-1 for the header
          Portals = new _Portal[PortalCount];
          for(int i = 0; i < PortalCount; i++)
          {
            sub = sub->next;
            parsePortal(Portals+i, sub);
          }
        }
        else if(string(sub->val) == "Terrain")
        {
          for(int i = 0; i < TerrainCount; i++)
          {
          }
          delete[] Terrains;
          TerrainCount =  sexp_list_length(expression)-1; //-1 for the header
          Terrains = new _Terrain[TerrainCount];
          for(int i = 0; i < TerrainCount; i++)
          {
            sub = sub->next;
            parseTerrain(Terrains+i, sub);
          }
        }
        else if(string(sub->val) == "Unit")
        {
          for(int i = 0; i < UnitCount; i++)
          {
          }
          delete[] Units;
          UnitCount =  sexp_list_length(expression)-1; //-1 for the header
          Units = new _Unit[UnitCount];
          for(int i = 0; i < UnitCount; i++)
          {
            sub = sub->next;
            parseUnit(Units+i, sub);
          }
        }
        else if(string(sub->val) == "UnitType")
        {
          for(int i = 0; i < UnitTypeCount; i++)
          {
            delete[] UnitTypes[i].name;
          }
          delete[] UnitTypes;
          UnitTypeCount =  sexp_list_length(expression)-1; //-1 for the header
          UnitTypes = new _UnitType[UnitTypeCount];
          for(int i = 0; i < UnitTypeCount; i++)
          {
            sub = sub->next;
            parseUnitType(UnitTypes+i, sub);
          }
        }
      }
      if(turnNumber % 2 == playerID) return 1;
    }
  }
}

DLLEXPORT _Building* getBuilding(int num)
{
  return Buildings + num;
}
DLLEXPORT int getBuildingCount()
{
  return BuildingCount;
}

DLLEXPORT _BuildingType* getBuildingType(int num)
{
  return BuildingTypes + num;
}
DLLEXPORT int getBuildingTypeCount()
{
  return BuildingTypeCount;
}

DLLEXPORT _Portal* getPortal(int num)
{
  return Portals + num;
}
DLLEXPORT int getPortalCount()
{
  return PortalCount;
}

DLLEXPORT _Terrain* getTerrain(int num)
{
  return Terrains + num;
}
DLLEXPORT int getTerrainCount()
{
  return TerrainCount;
}

DLLEXPORT _Unit* getUnit(int num)
{
  return Units + num;
}
DLLEXPORT int getUnitCount()
{
  return UnitCount;
}

DLLEXPORT _UnitType* getUnitType(int num)
{
  return UnitTypes + num;
}
DLLEXPORT int getUnitTypeCount()
{
  return UnitTypeCount;
}


DLLEXPORT int getPlayer0Gold0()
{
  return player0Gold0;
}
DLLEXPORT int getPlayer0Gold1()
{
  return player0Gold1;
}
DLLEXPORT int getPlayer0Gold2()
{
  return player0Gold2;
}
DLLEXPORT int getPlayer1Gold0()
{
  return player1Gold0;
}
DLLEXPORT int getPlayer1Gold1()
{
  return player1Gold1;
}
DLLEXPORT int getPlayer1Gold2()
{
  return player1Gold2;
}
DLLEXPORT int getPlayerID()
{
  return playerID;
}
DLLEXPORT int getTurnNumber()
{
  return turnNumber;
}

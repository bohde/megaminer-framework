//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that

#include <iostream>
#include <cstring>

#include "AI.h"
#include "network.h"
#include "game.h"
#include "sexp/sexp.h"

using namespace std;

extern "C"
{
extern char** _argv;
extern int    _argc;
}

int main(int argc, char** argv)
{
   _argv = argv;
   _argc = argc;

  bool practice = false;
  if(argc < 2)
  {
    cout<<"Please enter a host name."<<endl;
    return 1;
  }

  const char* message;
  sexp_t* expression;
  AI ai;
  int socket = open_server_connection(argv[1], "19000");
  if(socket == -1)
  {
    cerr << "Unable to connect to server" << endl;
    return 1;
  }
  if(!login(socket, ai.username(), ai.password()))
  {
    return 1;
  }

  if(argc < 3)
  {
    createGame();
  }
  else
  {
    if (strcmp(argv[2], "practice")==0)
    {
      createGame();
      practice = true;
    }
    else
    {
      joinGame(atoi(argv[2]));
    }
  }
  while(networkLoop(socket, practice))
  {
    if(ai.startTurn() && !(ai.turnNum() == 1 && !isHuman()))
    {
      endTurn();
    }
    else if(!(ai.turnNum() == 1 && !isHuman()))
    {
      getStatus();
    }
  }
  //Wait for log
  while (networkLoop(socket)){}
  return 0;
}

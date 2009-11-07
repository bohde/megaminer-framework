import time
import sys
from stat import *
import os
import string
import dircache
import shutil
import tempfile
import random
import copy
import subprocess
import threading

def run(program, *args):
    if (os.environ.get('OSTYPE') == 'linux'):
        ext = ""
    else:
        ext = ".exe"
    
    for path in string.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program)
        if not file.endswith(ext):
            file = file + ext
        try:
            return subprocess.Popen((file,) + args)        
        except os.error:
            pass
    file = os.path.join(os.path.abspath("."), program)
    if not file.endswith(ext):
        file = file + ext
    try:
        return subprocess.Popen((file,) + args)        
    except os.error:
        pass
    print file
    raise os.error, "cannot find executable"

def _scramble_list( l ):
    l = copy.copy(l)
    random.shuffle(l)
    "return a scrambled version of the list l."
    return l

class Arena:
    #runClients and runVis are boolean values
    def __init__(self, runMatches, runVis):
        self.runMatches = runMatches
        self.runVis = runVis
        if self.runMatches:
            self.MaxClientsRunning = 2
        self.maxBackLogs = 4
    
    def newTournament(self):
        self.matchup = []
        list = dircache.listdir("clients")
        for f in list:
            if f.startswith("."):
                list.remove(f)
        if len(list) > 1:
            try:
                for clientA in list:
                    shutil.copy("clients/" +  clientA, "arena/" + clientA)
                    for clientB in list:
                        if (clientA != clientB):
                            self.matchup.append([str(clientA), str(clientB)])
                self.matchup = _scramble_list(self.matchup)
                file('records.dat', 'a').write('New Arena Tournament Started\n')
            except IOError:
                print "Error while copying clients.  Tournament delayed."
                self.matchup = []


    def startNextMatch(self):
        print "Starting " + self.matchup[0][0] + " vs " + self.matchup[0][1]
        #self.clientProc.append(run("arena/" + self.matchup[0][0], "localhost"))
        self.startClient(self.matchup[0][0], True)
        time.sleep(5)
        #self.clientProc.append(run("arena/" + self.matchup[0][1], "localhost", str(self.gameNumber)))
        self.startClient(self.matchup[0][1], False)
        time.sleep(5)
        self.gameNumber += 1
        self.matchup.pop(0)

    def startClient(self, filename, isNewGame):
        if filename.endswith(".cpp.client"):
            if isNewGame:
                self.clientProc.append(run("arena/" + filename, 
                                          "localhost"))
            else:
                self.clientProc.append(run("arena/" + filename,
                                           "localhost", str(self.gameNumber)))
        elif filename.endswith(".java.client.tar.gz"):
            if isNewGame:
                self.clientProc.append(run("runJava", 
                                   "" + filename.replace(".tar.gz",''),
                                    "localhost"))
            else:
                self.clientProc.append(run("runJava",
                                   "" + filename.replace(".tar.gz",''),
                                   "localhost", str(self.gameNumber)))
        else: #Python
            if isNewGame:
                self.clientProc.append(run("runPython", 
                                   "" + filename.replace(".tar.gz",''),
                                   "localhost"))
            else:
                self.clientProc.append(run("runPython", 
                                   ""+ filename.replace(".tar.gz",''),
                                   "localhost", str(self.gameNumber)))
         

    def tryVisualizing(self):
        oldest = int(sys.maxint)
        files = dircache.listdir(".")
        oldestLog = ""
        for log in files:
            if (log.endswith(".gamelog") and os.stat(log)[ST_MTIME] < oldest):
                oldest = os.stat(log)[ST_MTIME]
                oldestLog = log
        if (len(oldestLog) > 0 and self.visProc is None):
            shutil.move(oldestLog, ".\\played\\" + oldestLog)
            self.visProc = run("visualizer", "-f", ".\\played\\" + oldestLog)

    def begin(self):
        self.serverProc = None #server process
        self.visProc = None #visualizer process or none
        self.gameNumber = 0
        self.matchup = []
        self.clientProc = [] #list of client processes
        if self.runMatches:
            self.serverProc = run("python", "main.py", "-b")
            run("python", "fileserver.py")
            time.sleep(5)
        while True:
            if self.runVis:
                #Check if the visualizer is still running
                if (not self.visProc is None):
                    if (not self.visProc.poll() is None):
                        self.visProc = None
                if (self.visProc is None):
                    self.tryVisualizing()

            if self.runMatches:
                #Check if the clients are still running
                for cli in self.clientProc:
                    if (not cli.poll() is None):
                        self.clientProc.remove(cli)
                if (len(self.matchup) == 0):
                    self.newTournament()
                files = dircache.listdir(".")
                logs = []
                for file in files:
                    if file.endswith(".gamelog"):
                        logs.append(file)
                if (len(self.clientProc) <= self.MaxClientsRunning - 2
                    and len(self.matchup) > 0 and len(logs) < self.maxBackLogs):
                    self.startNextMatch()

            time.sleep(5)

        #close any clients that are still trying to run
        for cli in self.clientProc:
            if (cli.poll() is None):
                cli.kill()


mode = 0
while not (mode > 0 and mode < 4):
    print "Which part of the arena should I run?"
    print "    1. The matches (clients, server, fileserver)"
    print "    2. The visualizer"
    print "    3. Everything"
    mode = int(input())

files = dircache.listdir(".")
missing = []
needed = []
if mode >= 2:
    needed = ["visualizer.exe", "SDL.dll", "SDL_net.dll"]
for myFile in needed:
    if not myFile in files:
        missing.append(myFile)
if len(missing) > 0:
    print "I am missing some files."
    print "Build the visualizer first, and then copy the following files"
    print "to the same folder as me (arena.py)"
    for myFile in missing:
        print "   - " + myFile
else:
    ar = Arena(mode == 1 or mode == 3, mode == 2 or mode == 3)
    ar.begin()


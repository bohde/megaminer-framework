"""
    Class files for a game server, interacting with the redirect server.
    Copyright (C) 2009  Josh Bohde <josh.bohde@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""                                             

from networking.Client import Client
from filters.LogicFilter import SexprHandlerMixin
from statements.StatementUtils import require_login, require_length, dict_wrapper 
from window import Window
import sexpr.sexpr as sexpr

def MalformedAnimation(Exception):
    pass

def animation_defs():
    anims = {}
    anim_mapper = dict_wrapper(anims)

    @anim_mapper("add")
    @require_length(2)
    def add(self, expr):
        self.window.add(expr[1])

    @anim_mapper("remove")
    @require_length(2)
    def remove(self, expr):
        self.window.remove(self, expr[1])

    @anim_mapper("move")
    @require_length(4)
    def move(self, expr):
        self.window.move(self, *expr[1:])

    @anim_mapper("attack")
    @require_length(4)
    def attack(self, expr):
        self.window.attack(self, *expr[1:])

    @anim_mapper("hurt")
    @require_length(3)
    def hurt(self, expr):
        self.window.hurt(self, *expr[1:])

    @anim_mapper("build")
    @require_length(4)
    def build(self, expr):
        self.window.build(self, *expr[1:])

    @anim_mapper("train")
    @require_length(3)
    def train(self, expr):
        self.window.train(self, *expr[1:])

    return anims

def status_defs():
    statii = {}
    status_mapper = dict_wrapper(statii)

    @status_mapper("game")
    @require_length(4)
    def game(self, expr):
        return expr[1:]

    @status_mapper("UnitType")
    def unitType(self, expr):
        return expr[1:]

    @status_mapper("Portal")
    def portal(self, expr):
        return expr[1:]

    @status_mapper("Unit")
    def unit(self, expr):
        return expr[1:]
    
    @status_mapper("Terrain")
    def terrain(self, expr):
        def convert(l):
            return { "objectID" : l[0],
                     "location" : l[1:2],
                     "period" : ["far past", "past", "present"][int(l[3])],
                     "blockMove" : l[4],
                     "blockBuild" : l[5]
                }
        return [convert(x) for x in expr[1:]]
            
    @status_mapper("BuildingType")
    def buildingType(self, expr):
        return expr[1:]

    @status_mapper("Building")
    def building(self, expr):
        return expr[1:]

    return statii


def protocol():
    statements = {}
    mapper = dict_wrapper(statements)
    anim_defs = animation_defs()
    status_d = status_defs()

    @mapper("changed")
    def status(self, expr):
        st = {}
        for i in expr[1:]:
            if type(i) != list:
                raise Exception("Not a list!")
            try:
                print i
                st[i[0]] = status_d[i[0]](self, i)
            except Exception, e:
                print e
                raise Exception("Unhandled exception!")
        #self.window.updateStatus(st)

    @mapper("animations")
    def animations(self, expr):
        for i in expr[1:]:
            try:
                pass
               # anim_defs[i[0]](self, i)
            except Exception, e:
                print e
                raise Exception("Unhandled exception!")

    return statements

class VisualizerClient(Client, SexprHandlerMixin):
    """
    Glues the visualizer and protocol together
    """
    def __init__(self, *args, **kwargs):
        Client.__init__(self, *args, **kwargs)
        self.statements = protocol()
        self.window = Window()
    
    
class FileVisualizer(SexprHandlerMixin):
     def __init__(self, filename):
         self.statements = protocol()
#         self.window = Window()
         self.filename = filename

     def mainloop(self):
         with open(self.filename) as f:
             for line in f:
                 self.readRawSExpr(line)

     def writeOut(self, data):
         pass

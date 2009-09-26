import pygame
from pygame.locals import *
from window import Window


pygame.init()

x = Window()

status = {'farPast':{"Unit":[{'objectID':1, 'location':(0,0), 'hp':100, 'level':0, 'unitType':'civE', 'ownerIndex':0, 'actions':2, 'moves':5}]},
    'past':{"Unit":[{'objectID':2, 'location':(600,0), 'hp':100, 'level':0, 'unitType':'civE', 'ownerIndex':0, 'actions':2, 'moves':5}],
            "Terrain":[{'objectID':5, 'location':(120,120), 'blockMove':True, 'blockBuild':True}]},
    'present':{"Unit":[{'objectID':3, 'location':(0,300), 'hp':100, 'level':0, 'unitType':'civE', 'ownerIndex':1, 'actions':2, 'moves':5}],
                "Building":[{'objectID':4, 'location':(200,200), 'hp':100, 'level':2, 'buildingType': 'gallery', 'ownerIndex':0, 'inTraining':False, 'progress':0, 'linked':0, 'complete':False}]}}

x.updateStatus(status)

i = 0
"""
x.add(3)
x.add(1)
x.add(2)
x.add(5)
x.add(4)
x.updateScreen()
"""
while pygame.event.poll().type != QUIT:
    if pygame.event.poll().type == KEYDOWN:
        x.move(1, i, i)
        x.updateScreen()
        i+=48
    if pygame.event.poll().type == MOUSEBUTTONDOWN:
        x.focusOn('present')
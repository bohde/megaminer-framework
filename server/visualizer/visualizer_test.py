import pygame
from pygame.locals import *
from window import Window


pygame.init()

x = Window()

status = {'farPast':{"Unit":[{'objectID':1, 'location':(0,0), 'hp':100, 'level':0, 'unitType':'civE', 'ownerIndex':0, 'actions':2, 'moves':5}]},
    'past':{"Unit":[{'objectID':2, 'location':(0,0), 'hp':100, 'level':0, 'unitType':'artil', 'ownerIndex':0, 'actions':2, 'moves':5}],
            "Terrain":[{'objectID':5, 'location':(1,1), 'blockMove':True, 'blockBuild':True}]},
    'present':{"Unit":[{'objectID':3, 'location':(19,19), 'hp':100, 'level':0, 'unitType':'civE', 'ownerIndex':1, 'actions':2, 'moves':5}],
                "Building":[{'objectID':4, 'location':(2,2), 'hp':100, 'level':2, 'buildingType': 'gallery', 'ownerIndex':0, 'inTraining':False, 'progress':0, 'linked':0, 'complete':False}]}}

x.updateStatus(status)

i = 1
#j = 

x.add(3)
x.add(1)
x.add(2)
#x.add(5)
x.add(4)
x.updateScreen()

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            x.move(1, i, i)
            #x.move(2,i,i)
            #x.hurt(2, 10)       
            i+=1
        elif event.type == MOUSEBUTTONDOWN:
            x.attack(2,0,0)
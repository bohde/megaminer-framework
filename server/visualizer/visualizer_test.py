import pygame
from pygame.locals import *
from window import Window


pygame.init()

x = Window()

status = {'present':{"Unit":[{'objectID':1, 'location':(0,0), 'hp':100, 'level':0, 'unitType':'pig', 'ownerIndex':0, 'actions':2, 'moves':5}]},
    'past':{"Unit":[{'objectID':2, 'location':(9,9), 'hp':100, 'level':0, 'unitType':'artil', 'ownerIndex':0, 'actions':2, 'moves':5},
                    {'objectID':3, 'location':(0,0), 'hp':100, 'level':0, 'unitType':'civE', 'ownerIndex':1, 'actions':2, 'moves':5}],
            "Terrain":[{'objectID':5, 'location':(1,1), 'blockMove':True, 'blockBuild':True}],
            "Building":[{'objectID':4, 'location':(2,2), 'hp':100, 'level':2, 'buildingType': 'gallery', 'ownerIndex':0, 'inTraining':False, 'progress':0, 'linked':0, 'complete':False}]}}

newstatus = {'past':{"Building":[{'objectID':4, 'location':(2,2), 'hp':100, 'level':2, 'buildingType': 'gallery', 'ownerIndex':0, 'inTraining':False, 'progress':0, 'linked':0, 'complete':True}]}}

x.updateStatus(status)

presentFocus = False

i = 9
j = 9

x.add(3)
x.add(1)
x.add(2)
x.add(5)
x.add(4)
x.updateScreen()

while True:
    changed = False
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit
            if event.key == K_SPACE:
                if not presentFocus:
                    x.focusOn('present')
                    presentFocus = True
                else:
                    x.focusOn('past')
                    presentFocus = False
            if event.key == K_UP:
                j+=1
                changed = True
            elif event.key == K_DOWN:
                j-=1
                changed = True
            elif event.key ==K_RIGHT:
                i+=1
                changed = True
            elif event.key == K_LEFT:
                i-=1
                changed = True
            elif event.key == K_RETURN:
                x.build(3,9,9)
            elif event.key == K_a:
                print "updatin' status"
                x.updateStatus(newstatus)
                x.add(4)
                x.updateScreen()
            if changed:
                try:
                    x.move(2,i,j)
                except:
                    pass
        elif event.type == MOUSEBUTTONDOWN:
            x.attack(2,0,0)
            
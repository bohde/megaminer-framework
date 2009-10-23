import pygame
from pygame.locals import *
from window import Window
from statusParser import statusParser


pygame.init()

x = Window()
"""
status = {'present':{"Unit":[{'objectID':1, 'location':(0,0), 'hp':100, 'level':0, 'unitType':'pig', 'ownerIndex':0, 'actions':2, 'moves':5}]},
    'past':{"Unit":[{'objectID':2, 'location':(9,9), 'hp':100, 'level':0, 'unitType':'artil', 'ownerIndex':0, 'actions':2, 'moves':5},
                    {'objectID':3, 'location':(0,0), 'hp':100, 'level':0, 'unitType':'civE', 'ownerIndex':1, 'actions':2, 'moves':5}],
            "Terrain":[{'objectID':5, 'location':(1,1), 'blockMove':True, 'blockBuild':True}],
            "Building":[{'objectID':4, 'location':(2,2), 'hp':100, 'level':2, 'buildingType': 'gallery', 'ownerIndex':0, 'inTraining':False, 'progress':0, 'linked':0, 'complete':False}]}}

newstatus = {'past':{"Building":[{'objectID':4, 'location':(2,2), 'hp':100, 'level':2, 'buildingType': 'gallery', 'ownerIndex':0, 'inTraining':False, 'progress':0, 'linked':0, 'complete':True}]}}
"""

status = statusParser('("changed" ("game" 0 (0 0 0) (0 0 0)) ("UnitType" (0 "Cavalry" 120 5 4 1500 50 5 2 0 280 0 1 7 0) (1 "Artist" 75 3 3 500 20 2 1 1 0 1 0 9 1) (2 "Artillery" 177 5 5 1800 25 3 1 2 750 3 4 7 0) (3 "Pig" 50 1 1 1600 130 3 0 1 0 1 0 6 0) (4 "Spearman" 181 5 3 2000 160 4 1 1 450 0 2 7 0) (5 "Engineer" 75 3 3 500 20 2 1 1 0 1 0 8 0)) ("Portal" (41 -9 -9 1 -1 20) (42 9 9 1 -1 20) (43 -9 -9 0 1 20) (44 9 9 0 1 20) (45 1 10 1 -1 20) (46 -1 -10 1 -1 20) (47 1 10 0 1 20) (48 -1 -10 0 1 20) (49 -7 3 1 -1 20) (50 7 -3 1 -1 20) (51 -7 3 0 1 20) (52 7 -3 0 1 20) (53 -2 8 1 -1 20) (54 2 -8 1 -1 20) (55 -2 8 0 1 20) (56 2 -8 0 1 20) (57 3 -1 1 -1 20) (58 -3 1 1 -1 20) (59 3 -1 0 1 20) (60 -3 1 0 1 20) (61 4 -7 1 -1 20) (62 -4 7 1 -1 20) (63 4 -7 0 1 20) (64 -4 7 0 1 20) (65 5 -4 1 1 20) (66 -5 4 1 1 20) (67 5 -4 2 -1 20) (68 -5 4 2 -1 20) (71 -8 1 1 1 20) (72 8 -1 1 1 20) (73 -8 1 2 -1 20) (74 8 -1 2 -1 20) (77 -6 -5 1 1 20) (78 6 5 1 1 20) (79 -6 -5 2 -1 20) (80 6 5 2 -1 20) (83 -9 2 1 1 20) (84 9 -2 1 1 20) (85 -9 2 2 -1 20) (86 9 -2 2 -1 20) (89 10 -2 1 1 20) (90 -10 2 1 1 20) (91 10 -2 2 -1 20) (92 -10 2 2 -1 20) (95 7 -10 1 1 20) (96 -7 10 1 1 20) (97 7 -10 2 -1 20) (98 -7 10 2 -1 20)) ("Unit" (20 4 1 0 500 0 5 0 1 2) (21 4 3 0 500 0 1 0 1 2) (22 4 1 1 500 0 5 0 1 2) (23 4 3 1 500 0 1 0 1 2) (24 4 1 2 500 0 5 0 1 2) (25 4 3 2 500 0 1 0 1 2) (35 -5 -2 0 500 0 5 1 0 0) (36 -5 -4 0 500 0 1 1 0 0) (37 -5 -2 1 500 0 5 1 0 0) (38 -5 -4 1 500 0 1 1 0 0) (39 -5 -2 2 500 0 5 1 0 0) (40 -5 -4 2 500 0 1 1 0 0)) ("Terrain" (69 5 -4 0 1 1) (70 -5 4 0 1 1) (75 -8 1 0 1 1) (76 8 -1 0 1 1) (81 -6 -5 0 1 1) (82 6 5 0 1 1) (87 -9 2 0 1 1) (88 9 -2 0 1 1) (93 10 -2 0 1 1) (94 -10 2 0 1 1) (99 7 -10 0 1 1) (100 -7 10 0 1 1) (101 -3 -1 0 1 1) (102 3 1 0 1 1) (103 3 10 0 1 1) (104 -3 -10 0 1 1) (105 4 8 0 1 1) (106 -4 -8 0 1 1) (107 9 1 0 1 1) (108 -9 -1 0 1 1) (109 2 -3 0 1 1) (110 -2 3 0 1 1) (111 -7 9 0 1 1) (112 7 -9 0 1 1) (113 9 1 1 1 1) (114 -9 -1 1 1 1) (115 -10 4 1 1 1) (116 10 -4 1 1 1) (117 4 9 1 1 1) (118 -4 -9 1 1 1) (119 -10 -1 1 1 1) (120 10 1 1 1 1) (121 -1 6 1 1 1) (122 1 -6 1 1 1) (123 -3 -9 1 1 1) (124 3 9 1 1 1) (125 8 0 2 1 1) (126 -8 0 2 1 1) (127 1 -4 2 1 1) (128 -1 4 2 1 1) (129 7 3 2 1 1) (130 -7 -3 2 1 1) (131 -10 -4 2 1 1) (132 10 4 2 1 1) (133 5 -5 2 1 1) (134 -5 5 2 1 1) (135 4 8 2 1 1) (136 -4 -8 2 1 1)) ("Building" (11 4 1 0 3500 0 8 0 -1 0 1 1) (12 4 1 1 3850 1 8 0 -1 0 1 1) (13 4 1 2 4235 2 8 0 -1 0 0 1) (14 4 3 0 3500 0 9 0 -1 0 1 1) (15 4 3 1 3850 1 9 0 -1 0 1 1) (16 4 3 2 4235 2 9 0 -1 0 0 1) (17 4 5 0 3000 0 6 0 -1 0 1 1) (18 4 5 1 3300 1 6 0 -1 0 1 1) (19 4 5 2 3630 2 6 0 -1 0 0 1) (26 -5 -6 0 3000 0 6 1 -1 0 1 1) (27 -5 -6 1 3300 1 6 1 -1 0 1 1) (28 -5 -6 2 3630 2 6 1 -1 0 0 1) (29 -5 -4 0 3500 0 9 1 -1 0 1 1) (30 -5 -4 1 3850 1 9 1 -1 0 1 1) (31 -5 -4 2 4235 2 9 1 -1 0 0 1) (32 -5 -2 0 3500 0 8 1 -1 0 1 1) (33 -5 -2 1 3850 1 8 1 -1 0 1 1) (34 -5 -2 2 4235 2 8 1 -1 0 0 1)) ("BuildingType" (6 "Farm" 300 10 7 4 2 3000 100 5 0 2 2 0 0) (7 "Barracks" 400 0 12 8 5 3500 100 5 0 2 2 0 0) (8 "School" 400 0 12 8 4 3500 100 5 0 2 2 0 0) (9 "Gallery" 400 0 8 5 3 3500 100 5 1 2 2 0 0) (10 "Bunker" 300 0 14 8 4 5000 100 5 0 2 2 0 0)))')

x.updateStatus(status.parse())

presentFocus = False
'''
i = 9
j = 9


x.add(3)
x.add(1)
x.add(2)
x.add(5)
x.add(4)
'''

x.add(69)

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
            """
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
        """
            
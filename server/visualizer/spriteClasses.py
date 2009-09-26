import pygame,os
from pygame.locals import *


unitImages = {"civE":{'0':[], '1':[]}, "art":{'0':[], '1':[]},"spear":{'0':[], '1':[]}, "artil":{'0':[], '1':[]}}
    #"cav":[cavStand, cavStep], "pig":[pigStand, pigStep]}

buildingImages = {"school":{'0':[], '1':[]}, "gallery":{'0':[], '1':[]}, "farm":{'0':[], '1':[]},
    "warFac":{'0':[], '1':[]}}  # ,"bunker":{'0':[], '1':[]}}

terrainImages = {"rock":[], "sand":[], "tree":[], "grass":[]}

tileSize = (60,70)

class Unit(pygame.sprite.Sprite):
    def __init__(self, objectID, location, hp, level, unitType, ownerIndex, actions, moves):
        pygame.sprite.Sprite.__init__(self)
        self.stand = unitImages[unitType][str(ownerIndex)][0].copy()
        self.step = unitImages[unitType][str(ownerIndex)][1].copy()
        self.image = self.stand
        self.rect = self.stand.get_rect()
        self.rect.topleft = location
        self.objectID = objectID
        self.unitTupe = unitType
        self.hp = hp
        self.level = level
        self.ownerIndex = ownerIndex
        self.actions = actions
        self.moves = moves
    
    def update(self):
        pass
        
    

class Building(pygame.sprite.Sprite):
    def __init__(self, objectID, location, hp, level, buildingType, ownerIndex, inTraining, progress, linked, complete):
        pygame.sprite.Sprite.__init__(self)
        self.construction = buildingImages[buildingType][str(ownerIndex)][0].copy()
        self.done = buildingImages[buildingType][str(ownerIndex)][1].copy()
        self.image = self.construction
        self.rect = self.construction.get_rect()
        self.rect.topleft = location
        self.objectID = objectID
        self.buildingType = buildingType
        self.hp = hp
        self.level = level
        self.ownerIndex = ownerIndex
        self.inTraining = inTraining
        self.progress = progress
        self.linked = linked
        self.complete = complete
    
    def update(self):
        if self.complete:
            self.image = self.done



class Terrain(pygame.sprite.Sprite):
    def __init__(self, objectID, location, blockMove, blockBuild):
        pygame.sprite.Sprite.__init__(self)
        if blockMove:
            if blockBuild:
                self.terrainType = 'rock'
            else:
                self.terrainType = 'tree'
        elif blockBuild:
            self.terrainType = 'sand'
        else:
            self.terrainType = 'grass'
        self.image = terrainImages[self.terrainType][0].copy()
        self.rect = self.image.get_rect()
        self.rect.midleft = location
        self.objectID = objectID
        self.blockMove = blockMove
        self.blockBuild = blockBuild

    

        
def loadAllImages():
        if not terrainImages['rock']:
            for name, images in terrainImages.iteritems():
                images.append(loadImage(name))
"""
      if not unitImages['civE']['0']:
            for name, players in unitImages.iteritems():
                for index, images in players.iteritems():
                    images.append(loadImage(name, index,"Stand"))
                    images.append(loadImage(name, index, "Step"))
        if not buildingImages['school']['0']:
            for name, players in buildingImages.iteritems():
                for index, images in players.iteritems():
                    images.append(loadImage(name, index,"Construction"))
                    images.append(loadImage(name, index, "Done"))
"""

def loadImage(name, ownerIndex = "", option = ""):
    path = os.path.join("sprites", ownerIndex+name+option+".png")
    try:
        image = pygame.image.load(path)
    except pygame.error, message:
        print "CANNOT LOAD IMAGE"
    image.set_colorkey(image.get_at((0,0)), RLEACCEL)
    return pygame.transform.scale(image.convert(), tileSize)
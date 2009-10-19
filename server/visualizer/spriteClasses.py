import pygame,os
from pygame.locals import *
from math import hypot


unitImages = {"civE":{'0':[], '1':[]}, "art":{'0':[], '1':[]},"spear":{'0':[], '1':[]}, "artil":{'0':[], '1':[]}, "blank":{'0':[], '1':[]},"pig":{'0':[], '1':[]}}
    #"cav":{'0':[], '1':[]}, }}

buildingImages = {"school":{'0':[], '1':[]}, "gallery":{'0':[], '1':[]}, "farm":{'0':[], '1':[]},
    "warFac":{'0':[], '1':[]}}  # ,"bunker":{'0':[], '1':[]}}

terrainImages = {"rock":[], "sand":[], "tree":[], "grass":[]}

class Unit(pygame.sprite.Sprite):
    def __init__(self, objectID, location, hp, level, unitType, ownerIndex, actions, moves):
        pygame.sprite.Sprite.__init__(self)
        self.stand = unitImages[unitType][str(ownerIndex)][0].copy()
        self.step = unitImages[unitType][str(ownerIndex)][1].copy()
        self.action = unitImages[unitType][str(ownerIndex)][2].copy()
        self.rect = self.stand.get_rect()
        self.rect.midbottom = location
        self.image = self.stand
        self.health = pygame.Surface((5,self.rect.height))
        self.working = False
        self.stepping = False
        self.attacking = False
        self.objectID = objectID
        self.unitType = unitType
        self.hp = hp
        self.level = level
        self.ownerIndex = ownerIndex
        self.actions = actions
        self.moves = moves
    
    def changeType(self, unitType):
        self.stand = unitImages[unitType][str(ownerIndex)][0].copy()
        self.step = unitImages[unitType][str(ownerIndex)][1].copy()
        self.action = unitImages[unitType][str(ownerIndex)][2].copy()
        self.unitType = unitType
    
    def update(self):
        if self.stepping:
            tempImage = self.step
        elif self.attacking:
            tempImage = self.action
            self.attacking = False
        elif self.working:
            if self.image == self.stand:
                tempImage = self.action
            else:
                tempImage = self.stand
        else:
            tempImage = self.stand
        
        if self.hp > 50:
            pygame.draw.rect(tempImage, [0,250,0], pygame.Rect(0,0,5,self.rect.height))
        elif self.hp <= 50 and self.hp >= 25:
            self.health.fill([0,0,0])
            pygame.draw.rect(tempImage, [229,97,5], pygame.Rect(0,0,5,self.rect.height/2))
        else:
            self.health.fill([0,0,0])
            pygame.draw.rect(tempImage, [250,0,0], pygame.Rect(0,0,5,self.rect.height/4))
                 
        if self.rect.midbottom[0] > 1280/2:
            tempImage = pygame.transform.flip(tempImage, True, False)
        
        self.image = tempImage
            

class Building(pygame.sprite.Sprite):
    def __init__(self, objectID, location, hp, level, buildingType, ownerIndex, inTraining, progress, linked, complete):
        pygame.sprite.Sprite.__init__(self)
        self.construction = buildingImages[buildingType][str(ownerIndex)][0].copy()
        self.done = buildingImages[buildingType][str(ownerIndex)][1].copy()
        self.rect = self.construction.get_rect()
        self.rect.midbottom = location
        self.image = self.construction
        self.health = self.image.subsurface(pygame.Rect(0,0,5,self.rect.height))
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
            
        if self.hp > 50:
            pygame.draw.rect(self.health, [0,250,0], pygame.Rect(0,0,5,self.rect.height))
        elif self.hp <= 50 and self.hp >= 25:
            self.health.fill([0,0,0])
            pygame.draw.rect(self.health, [229,97,5], pygame.Rect(0,0,5,self.rect.height*2/3))
        else:
            self.health.fill([0,0,0])
            pygame.draw.rect(self.health, [250,0,0], pygame.Rect(0,0,5,self.rect.height/3))



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
        self.rect.center = location
        self.objectID = objectID
        self.blockMove = blockMove
        self.blockBuild = blockBuild

    

        
def loadAllImages(tileSize):
    spriteSize = (tileSize[1], tileSize[1])
    if not terrainImages['rock']:
        for name, images in terrainImages.iteritems():
            images.append(loadImage(name, tileSize))       
    if not unitImages['civE']['0']:
        for name, players in unitImages.iteritems():
            for index, images in players.iteritems():
                images.append(loadImage(name, spriteSize, index,"Stand"))
                images.append(loadImage(name, spriteSize, index, "Step"))
                images.append(loadImage(name, spriteSize, index,"Action"))
    if not buildingImages['school']['0']:
        for name, players in buildingImages.iteritems():
            for index, images in players.iteritems():
                images.append(loadImage(name, tileSize, index,"Construction"))
                images.append(loadImage(name, tileSize, index, "Done"))
        

def loadImage(name, size, ownerIndex = "", option = "", key = True):
    path = os.path.join("sprites", ownerIndex+name+option+".png")
    try:
        image = pygame.image.load(path)
    except pygame.error, message:
        print "CANNOT LOAD IMAGE %(1)s" %{'1':(ownerIndex+name+option+".png")}
    if key:
        image.set_colorkey(image.get_at((0,0)), RLEACCEL)
    return pygame.transform.scale(image.convert(), size)

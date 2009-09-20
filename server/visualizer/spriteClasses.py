import pygame,os
from pygame.locals import *

spriteImages = {"civE":[], "art":[],"spear":[], "artil":[]}
    #"cav":[cavStand, cavStep], "pig":[pigStand, pigStep]}


class Unit(pygame.sprite.Sprite):
    def __init__(self, objectID, location, hp, level, unitType, ownerIndex, actions, moves):
        pygame.sprite.Sprite.__init__(self)
        if not spriteImages['civE']:
            for name, images in spriteImages.iteritems():
                images.append(loadImage(name,"Stand"))
                images.append(loadImage(name, "Step"))
        self.stand = spriteImages[unitType][0].copy()
        self.step = spriteImages[unitType][1].copy()
        self.rect = self.stand.get_rect()
        self.rect.topleft = location
        self.objectID = objectID
        self.hp = hp
        self.level = level
        self.ownerIndex = ownerIndex
        self.actions = actions
        self.moves = moves
        
    
"""
class CivE(Unit):
    def __init__(self, objectID, location, hp, level, ownerIndex, actions, moves):
        Unit.__init__(self, objectID, location, hp, level, 'civE', ownerIndex, actions, moves)
"""
    

def loadImage(name, standOrStep):
        path = os.path.join("sprites", name+standOrStep+".png")
        try:
            image = pygame.image.load(path)
        except pygame.error, message:
            print "CANNOT LOAD IMAGE"
        image.set_colorkey(image.get_at((0,0)), RLEACCEL)
        return image.convert()
        
    

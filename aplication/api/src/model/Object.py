from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
import pygame as pg
import numpy as np
from model import Aplication
from function import imageFunction

class ObjectTypes:
    APLICATION = 'aplication'
    CENARIO = 'cenario'
    STANDARD_OBJECT = 'standard_object'
    USER_INTERFACE = 'user_interface'

    types = {
        0 : 'aplication',
        10 : 'cenario',
        100 : 'standard_object',
        1000 : 'user_interface'
    }

    blitsOrder = (lambda types=types : { types[key]:key for key in types.keys() })()
    print(f'blitsOrder = {(lambda types=types : { types[key]:key for key in types.keys() })()}')

    def getType(typeIndex):
        return ObjectTypes.types[typeIndex]

    def getBlitOrder(object,father):
        if object.type == father.type :
            blitOrder = father.blitOrder + 1
        else :
            # blitOrder = list(ObjectTypes.types.keys())[list(ObjectTypes.types.values()).index(object.type)]
            blitOrder = ObjectTypes.blitsOrder[object.type]
        return blitOrder


class ObjectHandler:

    def __init__(self):
        self.objects = {}
        self.collidableObjects = {}
        self.collidableObjectsPosition = []

    def updateCollidableObjects(self):
        self.collidableObjects = {object.name:object for object in sorted(self.objects.values(),key=self.renderOrder) if object.collides}
        self.collidableObjectsPosition = [object.spaceCostRect for object in self.collidableObjects.values()]

    def renderOrder(self,object):
        return object.blitOrder,object.spaceCostRect.bottom

    def addNewObject(self,object):
        self.objects[object.name] = object


class Object:
    '''
    It's a object'''
    def __init__(self,name,position,size,scale,velocity,father,aplication,
            type = None,
            collidableSize = None,
            imagePath = None,
            soundPath = None
        ):
        '''
        Object()'''
        self.name = name
        if type :
            self.type = type
        else :
            self.type = ObjectTypes.STANDARD_OBJECT

        self.father = father
        self.blitOrder = ObjectTypes.getBlitOrder(self,father=self.father)
        print(f'{self.name} object type is {self.type} and its blit order is {self.blitOrder}')

        self.size = size.copy()
        self.scale = scale
        self.scaleFactor = (self.scale * aplication.size[1]) / (aplication.scaleRange * self.size[1])
        self.size[0] = int(np.ceil(self.size[0] * self.scaleFactor))
        self.size[1] = int(np.ceil(self.size[1] * self.scaleFactor))

        self.position = position ###- self.getPosition() #
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])

        ###- print(f'imagePath = {imagePath}')
        if imagePath :
            self.imagePath = imagePath + self.name + '.png'
        else :
            self.imagePath = aplication.imagePath + self.type + '/' + self.name + '.png'
        ###- print(f'object.imagePath = {self.imagePath}')
        self.image = imageFunction.getImage(self.imagePath,self.size,aplication)
        self.imageSurface = imageFunction.newImageSurface(self.image,self.size)

        self.soundPath = soundPath

        if collidableSize :
            self.collidableSize = collidableSize.copy()
            self.collides = True
        else :
            self.collidableSize = size.copy()
            self.collides = False
        self.collidableSize[0] = int(np.ceil(self.collidableSize[0] * self.scaleFactor))
        self.collidableSize[1] = int(np.ceil(self.collidableSize[1] * self.scaleFactor))
        self.spaceCostRect = pg.Rect(
            self.position[0],
            self.position[1]+self.size[1]-self.collidableSize[1],
            self.collidableSize[0],
            self.collidableSize[1]
        )

        self.velocity = velocity * aplication.velocityControl

        self.objectHandler = ObjectHandler()
        father.objectHandler.addNewObject(self)
        ###- print(f'{self.name} created successfully')

    def updatePosition(self,move,aplication):
        '''
        It updates the object position
        updatePosition(move,aplication)'''
        if move[0]!=0 or move[1]!=0 :
            module = ( (move[0]**2+move[1]**2)**(1/2) ) / self.velocity
            xMovement = move[0]/module
            yMovement = move[1]/module
            self.spaceCostRect.move_ip(xMovement,yMovement)
            if self.itColided(aplication) :
                self.spaceCostRect.move_ip(-xMovement,-yMovement)
                self.position = self.getPosition()
            else :
                self.rect.move_ip(xMovement,yMovement)

    def itColided(self,aplication):
        if self.collides :
            colisionIndexes = self.spaceCostRect.collidelistall(aplication.spaceCostObjectsPositionRectList)
            if list(aplication.collidableObjects.keys()).index(self.name) in colisionIndexes :
                return len(colisionIndexes)>1
            return len(colisionIndexes)>0
        return False

    def getPosition(self):
        return [self.rect[0],self.rect[1]] ###- upper left corner

    def addNewObject(self,object,aplication):
        # self.objects[object.name] = object
        if object.name == aplication.name :
            aplication.objects[object.name] = object
        else :
            self.objects[object.name] = object

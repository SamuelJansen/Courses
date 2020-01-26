import pygame as pg

from model import Aplication
from model.input_output import Screen

from function import imageFunction, fatherFunction

import numpy as np

print('Object library imported')

class Object:

    def __init__(self,name,position,size,scale,velocity,father,
            type = None,
            collidableSize = None,
            imagePath = None,
            soundPath = None
        ):

        self.father = father
        self.aplication = self.father.aplication

        self.name = name
        if type :
            self.type = type
        else :
            self.type = ObjectTypes.STANDARD_OBJECT

        self.blitOrder = ObjectTypes.getBlitOrder(self)
        tab = '   '
        print(f'{self.name}\n{tab}object type: {self.type}\n{tab}blit order: {self.blitOrder}')

        self.size = size.copy()
        if scale :
            self.scale = scale
        else :
            self.scale = (self.aplication.scaleRange * self.size[1]) / self.aplication.size[1]
        self.scaleFactor = (self.scale * self.aplication.size[1]) / (self.aplication.scaleRange * self.size[1])
        self.size[0] = int(np.ceil(self.size[0] * self.scaleFactor))
        self.size[1] = int(np.ceil(self.size[1] * self.scaleFactor))

        self.position = position.copy()
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])

        ###- print(f'imagePath = {imagePath}')
        if imagePath :
            self.imagePath = f'{imagePath}{self.name}.png'
            print(f'    imagePath = {self.imagePath}')
        else :
            self.imagePath = f'{self.aplication.imagePath}{self.type}\\{self.name}.png'
        ###- print(f'object.imagePath = {self.imagePath}')
        self.image = imageFunction.getImage(self.imagePath,self.size,self.aplication)
        # self.originalScreenSurface = imageFunction.newImageSurface(self.image,self.size)
        # self.screenSurface = self.originalScreenSurface.copy()

        self.soundPath = soundPath

        if collidableSize :
            self.collidableSize = collidableSize.copy()
            self.collides = True
        else :
            self.collidableSize = size.copy()
            self.collides = False
        self.collidableSize[0] = int(np.ceil(self.collidableSize[0] * self.scaleFactor))
        self.collidableSize[1] = int(np.ceil(self.collidableSize[1] * self.scaleFactor))
        self.collidableRect = pg.Rect(
            self.position[0],
            self.position[1]+self.size[1]-self.collidableSize[1],
            self.collidableSize[0],
            self.collidableSize[1]
        )

        self.velocity = velocity * self.aplication.velocityControl

        self.screen = Screen.Screen(self)
        self.objectHandler = ObjectHandler(self)

        self.father.objectHandler.addNewObject(self)

        ###- print(f'{self.name} created successfully')

    def updatePosition(self,move):
        if move[0]!=0 or move[1]!=0 :
            module = ( (move[0]**2+move[1]**2)**(1/2) ) / self.velocity
            xMovement = move[0]/module
            yMovement = move[1]/module
            self.collidableRect.move_ip(xMovement,yMovement)
            if self.objectHandler.itColided(self) :
                self.collidableRect.move_ip(-xMovement,-yMovement)
            else :
                self.rect.move_ip(xMovement,yMovement)
                self.position = self.getPosition()

    def setPosition(self,position):
        self.position = position.copy()
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        self.collidableRect = pg.Rect(
            self.position[0],
            self.position[1]+self.size[1]-self.collidableSize[1],
            self.collidableSize[0],
            self.collidableSize[1]
        )
        self.father.mustUpdateNextFrame()

    def getPosition(self):
        return [self.rect[0],self.rect[1]] ###- upper left corner

    def setPosition(self,position):
        if self.position[0]!=position[0] or self.position[1]!=position[1] :
            self.position = position
            self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
            self.collidableRect = pg.Rect(
                self.position[0],
                self.position[1]+self.size[1]-self.collidableSize[1],
                self.collidableSize[0],
                self.collidableSize[1]
            )


class ObjectHandler:

    def __init__(self,object):
        self.object = object
        self.objects = {}
        self.collidableObjects = {}
        self.collidableObjectsRect = []

        self.originalPosition = self.object.position.copy()
        self.originalSize = self.object.size.copy()
        self.originalImage = self.object.image.copy()
        self.originalSurface = self.object.screen.surface.copy()

        if fatherFunction.isNotAplication(self.object) :
            self.object.father.objectHandler.addNewObject(self.object)


    def update(self):
        pass

    def itColided(self,object):
        if object.collides :
            colisionIndexes = object.collidableRect.collidelistall(self.collidableObjectsRect)
            if list(self.collidableObjects.keys()).index(object.name) in colisionIndexes :
                return len(colisionIndexes)>1
            return len(colisionIndexes)>0
        return False

    def updateCollidableObjects(self):
        self.collidableObjects = {object.name:object for object in sorted(self.objects.values(),key=self.renderOrder) if object.collides}
        self.collidableObjectsRect = [object.collidableRect for object in self.collidableObjects.values()]

    def renderOrder(self,object):
        return object.blitOrder,object.collidableRect.bottom

    def addNewObject(self,object):
        # print(f'======= {self.object.name}.objectHandler.addNewObject() --> function call ======')
        self.objects[object.name] = object
        self.object.screen.mustUpdateNextFrame()
        # print(f'=========== {object.name} object added to {self.object.name} object ======')
        # print(f'======= {self.object.name}.objectHandler.addNewObject() --> function resolved ======')

    def deleteObject(self,objectName):
        del self.objects[objectName]
        self.object.screen.mustUpdateNextFrame()


class ObjectTypes:
    APLICATION = 'aplication'
    APLICATION_FLOOR = 'aplication_floor'
    CENARIO = 'cenario'
    STANDARD_OBJECT = 'standard_object'
    USER_INTERFACE = 'user_interface'

    types = {
        0 : APLICATION,
        10 : APLICATION_FLOOR,
        100 : CENARIO,
        1000 : STANDARD_OBJECT,
        10000 : USER_INTERFACE
    }

    blitOrder = (lambda types=types : { types[key]:key for key in types.keys() })()
    # print(f'blitOrder = {(lambda types=types : { types[key]:key for key in types.keys() })()}')

    def getType(typeIndex):
        return ObjectTypes.types[typeIndex]

    def getBlitOrder(object):
        if object.type == object.father.type :
            blitOrder = object.father.blitOrder + 1
        else :
            # blitOrder = list(ObjectTypes.types.keys())[list(ObjectTypes.types.values()).index(object.type)]
            blitOrder = ObjectTypes.blitOrder[object.type]
        return blitOrder

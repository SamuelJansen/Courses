import pygame as pg

import Screen, Handler
import imageFunction, eventFunction

import numpy as np

print('Object library imported')

class Object:
    #'''
    NOT_SELECTABLE_COLOR = [0,0,0,0]
    NO_IMAGE_COLOR = [0,0,0,0]
    #'''
    '''
    NOT_SELECTABLE_COLOR = [0,0,100,40]
    NO_IMAGE_COLOR = [255,0,0,40]
    #'''

    SINGLE_CLICK_SELECTABLE = 'SINGLE_CLICK_SELECTABLE'
    DOUBLE_CLICK_SELECTABLE = 'DOUBLE_CLICK_SELECTABLE'

    def __init__(self,name,position,size,scale,velocity,father,
            type = None,
            functionKey = None,
            collidableSize = None,
            noImage = False,
            imagePath = None,
            soundPath = None
        ):

        self.father = father
        self.application = self.father.application

        self.name = name
        if type :
            self.type = type
        else :
            self.type = ObjectType.STANDARD_OBJECT

        self.blitOrder = ObjectType.getBlitOrder(self)
        tab = '   '
        print(f'{self.name}\n{tab}object type: {self.type}\n{tab}blit order: {self.blitOrder}')

        self.size = size.copy()
        if scale :
            self.scale = (self.application.scaleRange * self.size[1]) / self.application.size[1]
            self.scaleFactor = (self.scale * self.application.size[1]) / (self.application.scaleRange * self.size[1])
            self.size[0] = int(np.ceil(self.size[0] * self.scaleFactor))
            self.size[1] = int(np.ceil(self.size[1] * self.scaleFactor))
        else :
            self.scale = scale
            self.scaleFactor = 1

        self.position = position.copy()
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])

        if imagePath :
            self.imagePath = f'{imagePath}{self.name}.png'
            print(f'    imagePath = {self.imagePath}')
        else :
            self.imagePath = f'{self.application.imagePath}{self.type}\\{self.name}.png'

        self.image = self.newImage(noImage)

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

        self.selectable = True

        self.velocity = velocity * self.application.velocityControl

        self.text = None
        self.textPosition = None
        self.textList = []
        self.textPositionList = []
        self.font = None

        if functionKey :
            self.functionKey = eventFunction.getFunctionKey(functionKey)
            self.handleEvent = eventFunction.eventFunctions[self.functionKey]
            self.singleClickSelectable = self.handleEvent(Object.SINGLE_CLICK_SELECTABLE)
            self.doubleClickSelectable = self.handleEvent(Object.DOUBLE_CLICK_SELECTABLE)
        else :
            self.functionKey = None
            self.handleEvent = None
            self.singleClickSelectable = False
            self.doubleClickSelectable = False

        self.screen = Screen.Screen(self)
        self.handler = Handler.Handler(self)

        self.father.handler.addObject(self)

        ###- print(f'{self.name} created successfully')

    def newImage(self,noImage):
        self.noImage = noImage
        if self.noImage :
             return imageFunction.getNoImage(self.size,self.application)
        else :
            return imageFunction.getImage(self.imagePath,self.size,self.application)

    def addText(
        self,text,position,fontSize,
        fontStyle = None
    ):
        textPositionErrorCompensation = self.getTextPositionError()
        if not fontStyle :
            fontStyle = self.application.fontStyle
            print(f'Object.application.fontStyle = {self.application.fontStyle}')
        try :
            pg.font.init()
            self.font = pg.font.SysFont(fontStyle,fontSize)
            self.textList.append(self.font.render(text,False,(0, 0, 0)))
            self.textPositionList.append([
                position[0] + textPositionErrorCompensation[0],
                position[1] + textPositionErrorCompensation[1]
            ])
        except :
            print("TextFont module not initialized")
            self.deleteText()

    def getTextPositionError(self):
        return[0,-6]

    def deleteText(self):
        self.text = None
        self.textPosition = None
        self.textList = []
        self.textPositionList = []
        self.font = None

    def updatePosition(self,move):
        if move[0]!=0 or move[1]!=0 :
            module = ( (move[0]**2+move[1]**2)**(1/2) ) / self.velocity
            xMovement = move[0]/module
            yMovement = move[1]/module
            self.collidableRect.move_ip(xMovement,yMovement)
            if self.handler.itColided(self) :
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

    def updateSelectionStatus(self,newStatus):
        self.isSelected = newStatus


class ObjectType:
    APPLICATION = 'APPLICATION'
    APPLICATION_FLOOR = 'APPLICATION_FLOOR'
    CENARIO = 'CENARIO'
    OBJECT = 'OBJECT'
    USER_INTERFACE = 'USER_INTERFACE'

    types = {
        0 : APPLICATION,
        10 : APPLICATION_FLOOR,
        100 : CENARIO,
        1000 : OBJECT,
        10000 : USER_INTERFACE
    }

    blitOrder = ( lambda types=types : { types[key]:key for key in types.keys() } )()
    # print(f'blitOrder = {(lambda types=types : { types[key]:key for key in types.keys() })()}')

    def getType(typeIndex):
        return ObjectType.types[typeIndex]

    def getBlitOrder(object):
        if object.type == object.father.type :
            blitOrder = object.father.blitOrder + 1
        else :
            # blitOrder = list(ObjectType.types.keys())[list(ObjectType.types.values()).index(object.type)]
            blitOrder = ObjectType.blitOrder[object.type] + ObjectType.blitOrder[object.father.type]
        return blitOrder

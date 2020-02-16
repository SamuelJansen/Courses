import pygame as pg

import Screen, Handler
import imageFunction, eventFunction, objectFunction

import numpy as np

print('Object library imported')

class Object:

    def __init__(self,name,position,size,scale,velocity,father,
            type = None,
            eventFunction = None,
            collidableSize = None,
            noImage = False,
            imagePath = None,
            soundPath = None
        ):

        self.tutor = self.father = father
        self.application = self.father.application

        self.name = name
        if type :
            self.type = type
        else :
            self.type = objectFunction.Type.OBJECT

        self.blitOrder = objectFunction.getBlitOrder(self)

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
            # print(f'    imagePath = {self.imagePath}')
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

        self.velocity = velocity * self.application.velocityControl

        self.textPosition = None
        self.textList = []
        self.textPositionList = []
        self.font = None

        self.initializeInteractiability(eventFunction)

        self.screen = Screen.Screen(self)
        self.handler = Handler.Handler(self)

        self.focus = None

        self.father.handler.addObject(self)

        ###- print(f'{self.name} created successfully')

    def newImage(self,noImage):
        self.noImage = noImage
        if self.noImage :
             return imageFunction.getNoImage(self.size,self.application)
        else :
            return imageFunction.getImage(self.imagePath,self.size,self.application)

    def addText(self,text,position,fontSize,
        fontStyle = None
    ):
        textPositionErrorCompensation = self.getTextPositionError()
        if not fontStyle :
            fontStyle = self.application.fontStyle
            # print(f'Object.application.fontStyle = {self.application.fontStyle}')
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

    def getPosition(self):
        return [self.rect[0],self.rect[1]] ###- upper left corner

    def getAbsolutePosition(self):
        if self.father.type == objectFunction.Type.APPLICATION :
            return self.getPosition()
        else :
            position = self.getPosition()
            fatherAbsolutePosition = self.father.getAbsolutePosition()
            return [
                position[0] + fatherAbsolutePosition[0],
                position[1] + fatherAbsolutePosition[1]
            ]

    def getAbsoluteOriginalPosition(self):
        if self.type == objectFunction.Type.APPLICATION :
            return [0,0]
        elif self.father.type == objectFunction.Type.APPLICATION :
            return self.handler.getOriginalPosition()
        else :
            position = self.handler.getOriginalPosition()
            fatherAbsoluteOriginalPosition = self.father.getAbsoluteOriginalPosition()
            return [
                position[0] + fatherAbsoluteOriginalPosition[0],
                position[1] + fatherAbsoluteOriginalPosition[1]
            ]

    def initializeInteractiability(self,eventFunction):
        self.hit = False
        self.clickable = False
        self.eventFunction = None
        self.execute = None
        self.singleClickable = False
        self.doubleClickable = False

        if eventFunction :
            self.clickable = True
            self.clicked = False
            self.eventFunction = eventFunction
            self.singleClickable = True ###- self.eventFunction.TYPE == objectFunction.Attribute.SINGLE_CLICKABLE
            self.doubleClickable = False ###- self.eventFunction.TYPE == objectFunction.Attribute.DOUBLE_CLICKABLE

    def handleEvent(self,event):
        return self.eventFunction(event)

    def getFunctionAttributes(self,attribute):
        return self.handleEvent(attribute)

    def updateHitStatus(self,didHit):
        self.hit = didHit

    def updateClickedStatus(self,status):
        if self.clickable :
            self.clicked = status

    def isClicked(self):
        if self.clickable :
            return self.clicked
        return False

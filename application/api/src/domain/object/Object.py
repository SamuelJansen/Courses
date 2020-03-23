import pygame as pg

import Screen, Handler
import imageFunction, eventFunction, objectFunction, textFunction

import numpy as np

print('Object library imported')

class Object:

    def __init__(self,name,position,size,scale,velocity,father,
            type = None,
            text = None,
            textPosition = None,
            fontSize = None,
            collidableSize = None,
            onLeftClick = None,
            onMenuResolve = None,
            onHovering = None,
            noImage = False,
            surfaceColor = None,
            imagePath = None,
            audioPath = None
        ):

        self.tutor = self.father = father
        self.application = self.father.application

        self.name = name
        if type :
            self.type = type
        else :
            self.type = objectFunction.Type.OBJECT

        self.blitOrder = objectFunction.getBlitOrder(self)
        # print(f'{self.type}.name = {self.name}, blit order = {self.blitOrder}')

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
        else :
            self.imagePath = f'{imageFunction.getImagePath(self)}{self.name}.png'

        self.image = self.newImage(noImage)
        # print(f'{self.name}.newImage():')
        # print(f'        imagePath = {self.imagePath}')
        # print(f'        image = self.image = {self.image}')

        self.audioPath = audioPath

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
        self.visible = True

        self.velocity = velocity * self.application.velocityControl

        self.text = text
        self.fontSize = fontSize
        self.textPosition = textFunction.parsePosition(textPosition,self)
        self.textList = []
        self.textPositionList = []
        self.font = None
        self.addText(self.text,self.textPosition,self.fontSize,
            fontStyle = None
        )

        self.screen = Screen.Screen(self,surfaceColor)
        self.handler = Handler.Handler(self)

        self.initializeInteractiability(
            onLeftClick,
            onMenuResolve,
            onHovering
        )
        self.focus = None

        self.father.handler.addObject(self)

        ###- print(f'{self.name} created, father = {self.father.name}, tutor = {self.tutor.name}, type = {self.type}, blit order = {self.blitOrder}')
        ###-
        print(f'{self.name} created, father = {self.father.name}, tutor = {self.tutor.name}, class = {self.__class__.__name__}, surfaceColor = {surfaceColor}')

    def newImage(self,noImage):
        self.noImage = noImage
        if self.noImage :
            return imageFunction.getNoImage(self.size,self.application,
                color = objectFunction.Attribute.NO_IMAGE_COLOR
            )
        else :
            return imageFunction.getImage(self.imagePath,self.size,self.application)

    def addText(self,text,position,fontSize,
        fontStyle = None
    ):
        if text :
            textPositionErrorCompensation = self.getTextPositionError()
            if not fontStyle :
                fontStyle = self.application.fontStyle
                # print(f'Object.application.fontStyle = {self.application.fontStyle}')
            try :
                nightModeColor = (129,139,145)
                pg.font.init()
                self.font = pg.font.SysFont(fontStyle,fontSize)
                self.textList.append(self.font.render(text,False,nightModeColor))
                self.textPositionList.append([
                    position[0] + textPositionErrorCompensation[0],
                    position[1] + textPositionErrorCompensation[1]
                ])
            except :
                print("TextFont module not initialized")
                self.deleteText()

            # https://pygame-zero.readthedocs.io/en/stable/ptext.html
            # screen.draw.text("hello world", centery=50, right=300)
            # screen.draw.text("hello world", midtop=(400, 0))
            # Keyword arguments:
            #
            # top left bottom right
            # topleft bottomleft topright bottomright
            # midtop midleft midbottom midright
            # center centerx centery

    def getTextPositionError(self):
        return [0,0]

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
        position = self.getPosition()
        if self.father.type == objectFunction.Type.APPLICATION :
            return [position[0] - 1,position[1] - 1]
        else :
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

    def initializeInteractiability(self,
        onLeftClick,
        onMenuResolve,
        onHovering
    ):
        self.clickable = False
        self.onLeftClick = None
        self.onMenuResolve = None
        self.onHovering = None
        self.singleClickable = False
        self.doubleClickable = False

        self.updateOnLeftClick(onLeftClick)
        self.updateOnMenuResolve(onMenuResolve)
        self.updateOnHovering(onHovering)

    def updateOnLeftClick(self,onLeftClick):
        self.onLeftClick = onLeftClick
        if self.onLeftClick :
            self.clickable = True
            self.singleClickable = True
        else :
            self.singleClickable = False

    def updateOnMenuResolve(self,onMenuResolve):
        self.onMenuResolve = onMenuResolve

    def updateOnHovering(self,onHovering):
        self.onHovering = onHovering

    def getName(self):
        return self.name

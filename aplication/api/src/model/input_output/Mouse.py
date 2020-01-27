import pygame as pg

from model.object import Object
from model.object.user_interface import Button
from model.event import Event

print('Mouse library imported')

class Mouse:

    def __init__(self,aplication):
        '''
        Mouse.position is pondered by dev screen size'''
        self.aplication = aplication
        self.position = [0,0]
        self.devPosition = [0,0]
        self.updatePosition()
        self.scripArea = ''

        self.objectHitClickDown = None
        self.objectHitClickUp = None
        self.hit = None
        self.objectSelected = None

    def updatePosition(self):
        ###- It needs some work
        self.position = list(pg.mouse.get_pos())
        self.devPosition[0] = int(self.position[0]*self.aplication.devResize[0])
        self.devPosition[1] = int(self.position[1]*self.aplication.devResize[1])
        # self.setPosition(self.position)

    def events(self,event):
        '''It checks for mouse events and deal with it'''
        if event.type == pg.MOUSEBUTTONDOWN :
            self.objectHitClickDown = self.clickDown()
            self.hit = None
            self.scripArea = f'{self.devPosition[0]}x{self.devPosition[1]}'

        if event.type == pg.MOUSEBUTTONUP :
            self.objectHitClickUp = self.clickUp()
            self.hit = None
            self.scripArea += f'x{self.devPosition[0]}x{self.devPosition[1]}'
            print(f'mouse.scripArea = {self.scripArea}')
            self.resolveClick()

    def clickDown(self):
        self.updatePosition()
        self.getRecursiveColision(self.aplication)
        # print(f'mouse.objectHitClickDown = {self.hit}')
        print(f'    mouse.objectHitClickDown.name = {self.hit.name}, type = {self.hit.type}')
        return self.hit

    def clickUp(self):
        self.updatePosition()
        self.getRecursiveColision(self.aplication)
        # print(f'mouse.objectHitClickUp = {self.hit}')
        print(f'    mouse.objectHitClickUp.name = {self.hit.name}, type = {self.hit.type}')
        return self.hit

    def getRecursiveColision(self,object):
        if object.handler.objects.values() :
            objectHitList = []
            for objectSon in object.handler.objects.values() :
                objectHit = self.getColision(objectSon)
                if objectHit :
                    objectHitList.append(objectHit)
            # print(f'object.name = {object.name}, objectHitList:')
            # for objectHit in objectHitList :
            #     print(f'    {objectHit.name}')
            if objectHitList :
                for objectHit in objectHitList :
                    self.getRecursiveColision(objectHit)
            objectHit = self.getColision(object)
            if objectHit :
                print(self.hit)
                if not self.hit :
                    self.hit = objectHit
                elif objectHit.blitOrder > self.hit.blitOrder :
                    self.hit = objectHit
        else :
            objectHit = self.getColision(object)
            if objectHit :
                if not self.hit :
                    self.hit = objectHit
                elif objectHit.blitOrder > self.hit.blitOrder :
                    self.hit = objectHit

    def getColision(self,object):
        try :
            notSelectable = True
            pixelColor = object.screen.surface.get_at(self.position)
            notSelectable = (pixelColor[0] == Object.Object.NOT_SELECTABLE_COLOR[0]) and notSelectable
            notSelectable = (pixelColor[1] == Object.Object.NOT_SELECTABLE_COLOR[1]) and notSelectable
            notSelectable = (pixelColor[2] == Object.Object.NOT_SELECTABLE_COLOR[2]) and notSelectable
            notSelectable = (pixelColor[3] == Object.Object.NOT_SELECTABLE_COLOR[3]) and notSelectable
            selectable = not notSelectable
            print(f'object hit name = {object.name}, pixelColor = {pixelColor}')
            print(f'    selectable = {selectable}')
        except :
            selectable = True
        if object.rect.collidepoint(self.position) and selectable :
            return object

    def resolveClick(self):
        if self.objectHitClickDown == self.objectHitClickUp :
            self.objectSelected = self.objectHitClickUp
            print(f'  objectClicked.name = {self.objectSelected.name}')
            # for object in self.objectSelected.handler.objects.values() :
            #     print(f'            objectClicked son --> {object.name}')
            self.action(self.objectSelected)
            self.objectSelected = None

    def action(self,object):
        event = Event.Event(object)
        if event.className == Event.Event.BUTTON :
            object.run(event)

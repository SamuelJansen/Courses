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

    def updatePosition(self):
        ###- It needs some work
        self.position = list(pg.mouse.get_pos())
        self.devPosition[0] = int(self.position[0]*self.aplication.devResize[0])
        self.devPosition[1] = int(self.position[1]*self.aplication.devResize[1])
        # self.setPosition(self.position)

    def events(self,event):
        '''It checks for mouse events and deal with it'''
        if event.type == pg.MOUSEBUTTONDOWN :
            self.clickDown()
            self.scripArea = f'{self.devPosition[0]}x{self.devPosition[1]}'

        if event.type == pg.MOUSEBUTTONUP :
            self.clickUp()
            self.scripArea += f'x{self.devPosition[0]}x{self.devPosition[1]}'
            print(f'mouse.scripArea = {self.scripArea}')

    def action(self,object):
        event = Event.Event(object)
        if event.className == Event.Event.BUTTON :
            object.run(event)

    def clickDown(self):
        self.updatePosition()
        self.objectHitClickDown = self.getRecursiveColision(self.aplication)#.floor)
        print(f'mouse.objectHitClickDown = {self.objectHitClickDown}')
        print(f'    mouse.objectHitClickDown.name = {self.objectHitClickDown.name}, type = {self.objectHitClickDown.type}')

    def clickUp(self):
        self.updatePosition()
        self.objectHitClickUp = self.getRecursiveColision(self.aplication)#.floor)
        print(f'mouse.objectHitClickUp = {self.objectHitClickUp}')
        print(f'    mouse.objectHitClickUp.name = {self.objectHitClickUp.name}, type = {self.objectHitClickUp.type}')

        if self.objectHitClickDown == self.objectHitClickUp :
            self.action(self.objectHitClickUp)

    def getRecursiveColision(self,object):
        if object.objectHandler.objects.values() :
            for objectSon in object.objectHandler.objects.values() :
                objectHit = self.getRecursiveColision(objectSon)
                if objectHit :
                    return objectHit
            objectHit = self.getColision(object)
            if objectHit :
                return objectHit
        else :
            objectHit = self.getColision(object)
            if objectHit :
                return objectHit

    def getColision(self,object):
        if object.rect.collidepoint(self.position) :
            return object

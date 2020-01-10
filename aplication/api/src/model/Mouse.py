from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
import pygame as pg
from model import Object,Button

class Mouse():

    def __init__(self,aplication):
        '''
        Mouse.position is pondered by dev screen size'''
        self.position = [0,0]
        self.devPosition = [0,0]
        self.updatePosition(aplication)
        self.scripArea = ''

        self.objectHitClickDown = None
        self.objectHitClickUp = None

    def updatePosition(self,aplication):
        ###- It needs some work
        self.position = list(pg.mouse.get_pos())
        self.devPosition[0] = int(self.position[0]*aplication.devResize[0])
        self.devPosition[1] = int(self.position[1]*aplication.devResize[1])
        # self.setPosition(self.position)

    def events(self,event,aplication):
        '''It checks for mouse events and deal with it'''
        if event.type == pg.MOUSEBUTTONDOWN :
            self.clickDown(aplication)
            self.scripArea = f'{self.devPosition[0]}x{self.devPosition[1]}'

        if event.type == pg.MOUSEBUTTONUP :
            self.clickUp(aplication)
            self.scripArea += f'x{self.devPosition[0]}x{self.devPosition[1]}'
            print(f'mouse.scripArea = {self.scripArea}')

    def action(self,object,aplication):
        if object.__class__.__name__ == 'Button' :
            object.run(aplication)

    def clickDown(self,aplication):
        self.updatePosition(aplication)
        self.objectHitClickDown = self.getRecursiveColision(aplication.workstation)
        print(f'mouse.objectHitClickDown = {self.objectHitClickDown}')
        print(f'    mouse.objectHitClickDown.name = {self.objectHitClickDown.name}')

    def clickUp(self,aplication):
        self.updatePosition(aplication)
        self.objectHitClickUp = self.getRecursiveColision(aplication.workstation)
        print(f'mouse.objectHitClickUp = {self.objectHitClickUp}')
        print(f'    mouse.objectHitClickUp.name = {self.objectHitClickUp.name}')

        if self.objectHitClickDown == self.objectHitClickUp :
            self.action(self.objectHitClickUp,aplication)

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

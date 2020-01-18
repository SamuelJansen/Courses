import pygame as pg
from function import imageFunction, fatherFunction
from model import Object

class Screen:
    '''
    It blits all objects on the screen.surface'''
    def __init__(self,object):
        '''
        It blits all objects on the screen.surface'''

        self.object = object
        print(f'   {self.object.name}.screen --> __init__() call')

        self.surface = None
        if fatherFunction.isNotAplication(self.object) :
            self.originalSurface = imageFunction.newImageSurface(self.object.image,self.object.size)
            self.surface = self.originalSurface.copy()
        else :
            self.surface = pg.display.set_mode(self.object.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.SRCALPHA,32)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.SRCALPHA,32)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.SRCALPHA)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.SRCALPHA)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE)
            # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.DOUBLEBUF)
            # self.screenSurface = pg.display.set_mode(self.size)

        self.blitRect = self.getBlitRect()
        self.blitList = self.getBlitList()
        self.surface.blits(self.blitList)
        self.mustUpdate = None
        self.mustUpdateNextFrame()

        if fatherFunction.isNotAplication(self.object) :
            self.object.father.objectHandler.addNewObject(self.object)
        else :
            print(f'ELSE screen.object.name = {self.object.name}, screen.object.father.name = {self.object.father.name}')

        print(f'   {self.object.name}.screen --> __init__() resolved')

    def getBlitRect(self):
        return pg.Rect(
            0,
            0,
            self.object.size[0],
            self.object.size[1]
        )

    def getBlitList(self):
        return [
            (object.screen.surface,object.rect)
            for object in self.object.objectHandler.objects.values()
            if self.blitRect.colliderect(object.rect)
        ]

    def mustUpdateNextFrame(self):
        print(f'      {self.object.name}.screen.mustUpdateNextFrame() --> function call')
        self.mustUpdate = True
        if fatherFunction.isNotAplication(self.object) :
            self.object.father.screen.mustUpdateNextFrame()

        print(f'         {self.object.name}.screen.mustUpdate = {self.mustUpdate}')
        print(f'      {self.object.name}.screen.mustUpdateNextFrame() --> function resolved')

    def didUpdate(self):
        print(f'         {self.object.name}.screen.didUpdate() --> function call')
        self.mustUpdate = False
        print(f'         {self.object.name}.screen.didUpdate() --> function resolved')

    def update(self):
        print(f'{self.object.name}.screen.update() --> function call')
        print(f'   {self.object.name}.screen.mustUpdate = {self.mustUpdate}')
        if self.mustUpdate : # and self.object.type!=Object.ObjectTypes.APLICATION :

            print(f'   {self.object.name}.objectHandler.objects = {self.object.objectHandler.objects}')
            for object in self.object.objectHandler.objects.values() :
                if object.screen.mustUpdate :
                    object.screen.update()

            self.updateBlitRect() ###- precaution
            self.updateBlitList()
            if fatherFunction.isNotAplication(self.object) :
                self.reset()
            self.surface.blits(self.blitList)
        self.didUpdate()
        print(f'{self.object.name}.screen.update() --> function resolved\n')

    def updateBlitRect(self):
        self.blitRect = self.getBlitRect()

    def updateBlitList(self):
        self.blitList = self.getBlitList()
        for element in self.blitList :
            print(element[1])

    def reset(self):
        print(f'         {self.object.name}.screen.rest() --> function call')
        self.surface = self.originalSurface.copy()
        print(f'         {self.object.name}.screen.rest() --> function resolved')

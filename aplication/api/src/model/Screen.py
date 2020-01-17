import pygame as pg
from function import imageFunction
from model import Object

class Screen():
    '''
    It blits all objects on the screenSurface'''
    def __init__(self,object):
        '''
        It blits all objects on the screenSurface'''
        self.object = object
        self.blitRect = self.getBlitRect()
        self.blitList = self.getBlitList()
        self.object.screenSurface.blits(self.blitList)

    def getBlitRect(self):
        return pg.Rect(
            0,
            0,
            self.object.size[0],
            self.object.size[1]
        )

    def getBlitList(self):
        return [
            (object.screenSurface,object.rect)
            for object in self.object.objectHandler.objects.values()
            if self.blitRect.colliderect(object.rect)
        ]

    def update(self):
        print(f'Screen.update() --> function call of {self.object.name} object')
        for object in self.object.objectHandler.objects.values() :
            try :
                if object.mustUpdateScreen :
                    object.screen.update()
            except :
                print(f'Screem.update() --> Error in {object.name} object')

        if self.object.mustUpdateScreen : # and self.object.type!=Object.ObjectTypes.APLICATION :
            self.updateBlitRect() ###- precaution
            self.updateBlitList()
            print(f'Screen.update() --> function call of {self.object.name} object - updated')
            try :
                # self.object.screenSurface = imageFunction.newImageSurface(self.object.image,self.object.size)
                imageFunction.resetScreenSurface(self.object)
                # print(f'Screen.update() --> {self.object.name} object')
            except :
                print(f'Screen.update() --> Error reseting {self.object.name} object')
                pass
        self.object.screenSurface.blits(self.blitList)
        self.object.mustUpdateScreen = False

    def updateBlitRect(self):
        self.blitRect = self.getBlitRect()

    def updateBlitList(self):
        self.blitList = self.getBlitList()
        for element in self.blitList :
            print(element[1])

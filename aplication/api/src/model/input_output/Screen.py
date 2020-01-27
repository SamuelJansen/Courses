from function import imageFunction, fatherFunction

import pygame as pg

print('Screen library imported')

class Screen:
    '''
    It blits all objects on the screen.surface'''
    def __init__(self,object):
        '''
        It blits all objects on the screen.surface'''

        self.object = object

        self.surface = self.newSurface()
        self.blitRect = self.getBlitRect()
        self.blitList = []

        self.mustUpdateNextFrame()

    def newSurface(self):
        if fatherFunction.isNotAplication(self.object) :
            if self.object.noImage :
                print(f'Screen.object.name = {self.object.name}')
                return imageFunction.newAlphaSurface(self.object.size)
            else :
                return imageFunction.newImageSurface(self.object.image,self.object.size)
        else :
            return imageFunction.newDisplay(self.object.size)

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
            for object in self.object.handler.objects.values()
            if self.blitRect.colliderect(object.rect)
        ]

    def mustUpdateNextFrame(self):
        self.mustUpdate = True
        fatherFunction.fatherMustUpdateNextFrame(self.object)

    def didUpdate(self):
        self.mustUpdate = False

    def update(self):
        if self.mustUpdate :
            for object in self.object.handler.objects.values() :
                if object.screen.mustUpdate :
                    object.screen.update()

            self.updateBlitRect() ###- precaution
            self.updateBlitList()
            self.reset()
            self.blitText()
            self.surface.blits(self.blitList)
        self.didUpdate()

    def updateBlitRect(self):
        self.blitRect = self.getBlitRect()

    def updateBlitList(self):
        self.blitList = self.getBlitList()

    def reset(self):
        if fatherFunction.isNotAplication(self.object) :
            self.surface = self.object.handler.originalSurface.copy()

    def blitText(self):
        print(f'self.object.name = {self.object.name}')
        if self.object.textList :
            for textIndex in range(len(self.object.textList)) :
                self.surface.blit(
                    self.object.textList[textIndex],
                    self.object.textPositionList[textIndex]
                )

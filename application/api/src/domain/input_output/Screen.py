import pygame as pg

import ErrorEvent
import imageFunction, fatherFunction, applicationFunction, objectFunction

print('Screen library imported')

class Screen:

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

    def __init__(self,object,color):
        '''
        It blits all objects on the screen.surface'''

        self.object = object
        if not color :
            color = objectFunction.Attribute.NO_IMAGE_COLOR
        self.color = color
        # self.object.handler = None

        self.surface = self.newSurface()
        self.blitRect = self.getBlitRect()
        self.blitList = []

        self.mustUpdateNextFrame()

    def reset(self):
        if fatherFunction.isNotAplication(self.object) :
            self.surface = self.object.handler.originalSurface.copy()

    def newSurface(self):
        if fatherFunction.isNotAplication(self.object) :
            if self.object.noImage :
                return imageFunction.newAlphaSurface(self.object,
                    color = self.color
                )
            else :
                return imageFunction.newImageSurface(self.object)
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
            if self.blitRect.colliderect(object.rect) and object.visible
        ]

    def mustUpdateNextFrame(self):
        self.mustUpdate = True
        self.fatherMustUpdateNextFrame(self.object)

    def fatherMustUpdateNextFrame(self,object) :
        if fatherFunction.isNotAplication(object) and not object.father.screen.mustUpdate :
            object.father.screen.mustUpdateNextFrame()

    def didUpdate(self):
        self.mustUpdate = False

    def updateBlitRect(self):
        self.blitRect = self.getBlitRect()

    def updateBlitList(self):
        self.blitList = self.getBlitList()

    def blitText(self):
        if self.object.textList :
            for textIndex in range(len(self.object.textList)) :
                self.surface.blit(
                    self.object.textList[textIndex],
                    self.object.textPositionList[textIndex],
                )

    def revealObjects(self,objectNames):
        if objectNames :
            for objectName in objectNames :
                if objectName in self.object.handler.objects :
                    self.object.handler.objects[objectName].visible = True
                else :
                    ErrorEvent.ErrorEvent(None,
                        message = f'{objectName} not found in {self.object.name}.handler.objects'
                    )
            self.object.screen.mustUpdateNextFrame()

    def hideAllObjects(self):
        for object in self.object.handler.objects.values() :
            object.visible = False
        self.object.screen.mustUpdateNextFrame()

    def remove(self):
        imageFunction.removeObjectImageAndSurface(self.object)

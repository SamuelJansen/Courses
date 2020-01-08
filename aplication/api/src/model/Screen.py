import pygame as pg

class Screen():
    '''
    It blits all objects on the screenModule'''
    def __init__(self,aplication):
        '''
        It blits all objects on the screenModule'''
        aplication.screenModule.fill(aplication.color['backgroundColor'])
        self.blitRect = pg.Rect(
            0,
            0,
            aplication.size[0],
            aplication.size[1]
        )
        self.blitList = [
            (object.imageSurface,object.rect)
            for object in aplication.objectHandler.objects.values()
            # if self.blitRect.colliderect(object.rect)
        ]
        aplication.screenModule.blits(self.blitList)

    def updateRectToBlit(self,aplication):
        self.blitRect = pg.Rect(
            0,
            0,
            aplication.size[0],
            aplication.size[1]
        )

    def updateBlitList(self,aplication):
        self.blitList = [
            (object.imageSurface,object.rect)
            for object in aplication.objectHandler.objects.values()
            if self.blitRect.colliderect(object.rect)
        ]

    def blit(self,aplication):
        '''
        It blits all objects on the screenModule'''
        aplication.screenModule.fill(aplication.color['backgroundColor'])
        # self.blitRect(aplication) ###- precaution
        self.updateBlitList(aplication)
        aplication.screenModule.blits(self.blitList)

    def update(self,aplication):
        self.blit(aplication)
        pg.display.update(self.blitRect)

from model.object import Object

import pygame as pg
import os

imageLibrary = {}
def getImage(path,size,aplication) :
    '''
    It picks the image contained in the path
    and store it in a library.
    It also returns the     image.
    It works on mac and windows
    getImage(path)'''
    global imageLibrary
    image = imageLibrary.get(path)
    if image==None :
        try :
            canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
            image = pg.image.load(canonicalizedPath)#.convert_alpha()
            print(f'importing image: {canonicalizedPath}')
        except :
            path = f'{aplication.imagePath}standard_image.png'
            canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
            print(f'importing image: {canonicalizedPath}')
            image = pg.image.load(canonicalizedPath)#.convert_alpha()
        image = pg.transform.smoothscale(image,size)#.convert_alpha()
    imageLibrary[path] = image
    return image.copy()

def getNoImage(size,aplication) :
    path = f'{aplication.imagePath}standard_image.png'
    canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
    image = pg.image.load(canonicalizedPath)
    image = pg.transform.smoothscale(image,size).convert_alpha()
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            image.set_at([x,y],Object.Object.NO_IMAGE_COLOR)
    return image

def saveImage(image,path) :
    global imageLibrary
    pg.image.save(image, path)
    imageLibrary[path] = image
    return image

def newImageSurface(image,size) :
    screenSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF).convert_alpha()
    # imageSurface = pg.Surface(size,pg.HWSURFACE)
    # imageSurface = pg.Surface(size,pg.DOUBLEBUF)
    # imageSurface = pg.Surface(size)
    screenSurface.blit(image,[0,0])
    return screenSurface

def newDisplay(size) :
    newDisplay = pg.display.set_mode(size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.SRCALPHA,32)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.SRCALPHA,32)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.SRCALPHA)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.SRCALPHA)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE)
    # self.screenSurface = pg.display.set_mode(self.size,pg.NOFRAME|pg.DOUBLEBUF)
    # self.screenSurface = pg.display.set_mode(self.size)
    return newDisplay

def newAlphaSurface(size) :
    screenSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
    screenSurface.fill(Object.Object.NOT_SELECTABLE_COLOR)
    return screenSurface.convert_alpha()

def colorFilter(threshold,image) :
    # threshold = (0,0,0)
    colorThreshold = threshold
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            color = image.get_at([x,y])
            # print(color)
            if ( color.r > colorThreshold[0] and color.g > colorThreshold[1] and color.b > colorThreshold[2] ):
                image.set_at([x,y],[0,0,0,0])
    return image

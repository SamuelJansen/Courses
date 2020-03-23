import pygame as pg
import os

import objectFunction, setting

imageLibrary = {}
def getImage(path,size,aplication,
        padding = None
    ) :
    '''
    It picks the image contained in the path
    and store it in a library.
    It also returns the     image.
    It works on mac and windows
    getImage(path)'''
    global imageLibrary
    image = imageLibrary.get(path) ###- image = imageLibrary[path]
    if not image :
        size = size.copy()
        if padding :
            size = [
                size[0] - 2 * padding[0],
                size[1] - 2 * padding[1]
            ]
        # print(f'new imagePath = {path}')
        try :
            canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
            image = pg.image.load(canonicalizedPath)#.convert_alpha()
            # print(f'importing image: {canonicalizedPath}')
        except :
            path = f'{aplication.imagePath}standard_image.png'
            canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
            # print(f'importing image: {canonicalizedPath}')
            image = pg.image.load(canonicalizedPath)
        image = pg.transform.smoothscale(image,size)
    imageLibrary[path] = image
    return image

def getImagePath(object):
    return f'{object.application.imagePath}{object.type}//'

def getImageFileNames(imagesPath,imageExtension) :
    return setting.getFileNames(imagesPath,imageExtension)

def getNoImage(size,aplication,
    color = objectFunction.Attribute.NO_IMAGE_COLOR
) :
    path = f'{aplication.imagePath}standard_image.png'
    canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
    image = pg.image.load(canonicalizedPath)
    image = pg.transform.smoothscale(image,size).convert_alpha()
    image.fill(color)
    return image

def workWithSpecificPixels(image) :
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            image.set_at([x,y],objectFunction.Attribute.NO_IMAGE_COLOR)

def saveImage(image,path) :
    global imageLibrary
    pg.image.save(image, path)
    imageLibrary[path] = image
    return image

def newImageSurface(object) :
    screenSurface = pg.Surface(object.size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF).convert_alpha()
    # imageSurface = pg.Surface(size,pg.HWSURFACE)
    # imageSurface = pg.Surface(size,pg.DOUBLEBUF)
    # imageSurface = pg.Surface(size)
    screenSurface.blit(object.image,[0,0])
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

def newAlphaSurface(object,
    color = None
) :
    if not color :
        color = objectFunction.Attribute.NOT_HITTABLE_COLOR
    screenSurface = pg.Surface(object.size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
    screenSurface.fill(color)
    return screenSurface

def removeObjectImageAndSurface(object) :
    pass

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

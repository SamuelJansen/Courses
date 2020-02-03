import numpy as np

import Object

print('UserInterfaceSurface library imported')

class Surface(Object.Object):

    SQUARE = 'SQUARE'

    def __init__(self,name,position,size,father,
        functionKey = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        if padding :
            self.padding = padding
        else :
            self.padding = [0,0]

        self.userInterfaceSurface = self

        size = parseSize(size,father)
        velocity = 0.00001

        Object.Object.__init__(
            self,
            name,
            position,
            size,
            scale,
            velocity,
            father,
            type = Object.ObjectType.USER_INTERFACE,
            functionKey = functionKey,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = soundPath
        )

        print(f'                                    Surface.padding = {self.padding}')

def getSizeNotPadded(surface) :
    return surface.originalSize

def parseSize(size,father) :
    if size :
        sizeParsed = [None,None]
        for featureSizeIndex in range(len(size)) :
            featureSize = size[featureSizeIndex]
            sizeParsed = getFeatureSize(sizeParsed,featureSize,featureSizeIndex,size,father)
        return sizeParsed
    return None

def getFeatureSize(sizeParsed,featureSize,featureSizeIndex,size,father) :
    if featureSize.__class__.__name__ == 'str' :
        sizeParsed = getFeatureByPoligono(sizeParsed,featureSize,featureSizeIndex,size,father)
        sizeParsed = getFeatureByPercentage(sizeParsed,featureSize,featureSizeIndex,father)
        if not sizeParsed[featureSizeIndex] :
            sizeParsed[featureSizeIndex] = featureSize
            print(f'error : --> getFeatureSize()')
            print(f'    {size}.featureSize = {featureSize}')
    else :
        sizeParsed[featureSizeIndex] = featureSize
    return sizeParsed

def getFeatureByPoligono(sizeParsed,featureSize,featureSizeIndex,size,father) :
    if not sizeParsed[featureSizeIndex] :
        if featureSize == Surface.SQUARE :
            if featureSizeIndex == 0 :
                try :
                    sizeParsed[featureSizeIndex] = getFeatureSize(
                        sizeParsed,size[1],1,size,father
                    )[1]
                except :
                    pass
            elif featureSizeIndex == 1 :
                try :
                    sizeParsed[featureSizeIndex] = size[0]
                except :
                    pass
    return sizeParsed

def getFeatureByPercentage(sizeParsed,featureSize,featureSizeIndex,father) :
    if not sizeParsed[featureSizeIndex] :
        try :
            sizeParsed[featureSizeIndex] = int(np.round(int(featureSize[:-1])*father.size[featureSizeIndex]/100,0))
        except :
            pass
    return sizeParsed

def getSizePadded(size,padding) :
    if padding :
        sizePadded = [size[index]-2*padding[index] for index in range(len(size))]
        print(f'                sizePadded = {sizePadded}')
        return sizePadded
    else :
        return size

def getPositionPadded(position,padding) :
    if padding :
        positionPadded = [position[index]+padding[index] for index in range(len(position))]
        return positionPadded
    else :
        return position
import numpy as np

class Attribute:

    NAME = 'Surface'


class Types :

    SQUARE = 'SQUARE'


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
    else :
        sizeParsed[featureSizeIndex] = featureSize
    return sizeParsed

def getFeatureByPoligono(sizeParsed,featureSize,featureSizeIndex,size,father) :
    if not sizeParsed[featureSizeIndex] :
        if featureSize == Types.SQUARE :
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
        except : pass
    return sizeParsed

def getSizePadded(size,padding) :
    if padding :
        sizePadded = [size[index]-2*padding[index] for index in range(len(size))]
        return sizePadded
    else :
        return size

def getPositionPadded(position,padding) :
    if padding :
        positionPadded = [position[index]+padding[index] for index in range(len(position))]
        return positionPadded
    else :
        return position

def stashPadding(padding,father) :
    if padding :
        originalPadding = padding.copy()
    else :
        try :
            originalPadding = father.padding.copy()
        except :
            originalPadding = [0,0]
    padding = [0,0]
    return padding,originalPadding

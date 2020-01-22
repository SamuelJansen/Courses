from model import Object

def parseSize(size,father) :
    sizeParsed = [None,None]
    for featureSizeIndex in range(len(size)) :
        featureSize = size[featureSizeIndex]
        sizeParsed = getFeatureSize(sizeParsed,featureSize,featureSizeIndex,size,father)
    return sizeParsed

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
        if featureSize == UserInterface.SQUARE :
            if featureSizeIndex==0 :
                try :
                    sizeParsed[featureSizeIndex] = getFeatureSize(
                        sizeParsed,size[1],1,size,father
                    )[1]
                except :
                    pass
            elif featureSizeIndex==1 :
                try :
                    sizeParsed[featureSizeIndex] = size[0]
                except :
                    pass
    return sizeParsed

def getFeatureByPercentage(sizeParsed,featureSize,featureSizeIndex,father) :
    if not sizeParsed[featureSizeIndex] :
        try :
            sizeParsed[featureSizeIndex] = int(featureSize[:-1]) * father.size[featureSizeIndex] / 100
        except :
            pass
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

class UserInterface(Object.Object):
    SQUARE = 'square'

    def __init__(self,name,position,size,scale,father,
        padding = None,
        imagePath = None,
        soundPath = None
    ):

        velocity = 0.00001
        size = parseSize(size,father)
        size = getSizePadded(size,padding)
        position = getPositionPadded(position,padding)

        Object.Object.__init__(
            self,
            name,
            position,
            size,
            scale,
            velocity,
            father,
            type = Object.ObjectTypes.USER_INTERFACE,
            imagePath = imagePath,
            soundPath = soundPath
        )

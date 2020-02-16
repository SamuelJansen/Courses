import Surface
import surfaceFunction

print('UserInterface library imported')

class UserInterface(Surface.Surface):

    def __init__(self,name,position,size,father,
        externalEvent = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        if not padding :
            try :
                if father.userInterfaceSurface :
                    padding = father.userInterfaceSurface.padding
            except :
                padding = [0,0]

        position = surfaceFunction.getPositionPadded(position,padding)
        size = surfaceFunction.getSizePadded(
            surfaceFunction.parseSize(size,father),
            padding
        )

        Surface.Surface.__init__(
            self,name,position,size,father,
            externalEvent = externalEvent,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = soundPath
        )

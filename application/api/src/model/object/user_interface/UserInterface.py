import Surface

print('UserInterface library imported')

class UserInterface(Surface.Surface):

    def __init__(self,name,position,size,father,
        functionKey = None,
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

        position = Surface.getPositionPadded(position,padding)
        size = Surface.parseSize(size,father)
        size = Surface.getSizePadded(size,padding)

        Surface.Surface.__init__(
            self,name,position,size,father,
            functionKey = functionKey,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = soundPath
        )

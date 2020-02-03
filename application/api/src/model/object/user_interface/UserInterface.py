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

        self.originalSize = size.copy()
        size = Surface.getSizePadded(size,padding)
        position = Surface.getPositionPadded(position,padding)

        print( f'                       UserInterface.sizePadded = {size}')
        print( f'                       UserInterface.positionPadded = {position}')

        Surface.Surface.__init__(
            self,name,position,size,father,
            functionKey = functionKey,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = soundPath
        )

        try :
            self.userInterfaceSurface = father.userInterfaceSurface
        except :
            padding = [0,0]

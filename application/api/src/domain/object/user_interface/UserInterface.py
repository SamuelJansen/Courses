import Surface
import surfaceFunction

print('UserInterface library imported')

class UserInterface(Surface.Surface):

    def __init__(self,name,position,size,father,
        text = None,
        textPosition = None,
        fontSize = None,
        scale = None,
        padding = None,
        noImage = False,
        onLeftClick = None,
        onMenuResolve = None,
        onHovering = None,
        imagePath = None,
        audioPath = None
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
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            noImage = noImage,
            onLeftClick = onLeftClick,
            onMenuResolve = onMenuResolve,
            onHovering = onHovering,
            imagePath = imagePath,
            audioPath = audioPath
        )

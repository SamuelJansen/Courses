import Surface
import surfaceFunction

print('UserInterface library imported')

class UserInterface(Surface.Surface):

    def __init__(self,name,position,size,father,
        type = None,
        text = None,
        textPosition = None,
        fontSize = None,
        scale = None,
        padding = None,
        onLeftClick = None,
        onMenuResolve = None,
        onHovering = None,
        noImage = False,
        surfaceColor = None,
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
            type = type,
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            onLeftClick = onLeftClick,
            onMenuResolve = onMenuResolve,
            onHovering = onHovering,
            noImage = noImage,
            surfaceColor = surfaceColor,
            imagePath = imagePath,
            audioPath = audioPath
        )













        # getNoImage(size,aplication,
        #     color = objectFunction.Attribute.NO_IMAGE_COLOR
        # )

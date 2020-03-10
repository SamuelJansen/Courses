import UserInterface

print('Button library imported')

class Button(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        text = None,
        textPosition = None,
        fontSize = None,
        padding = None,
        onLeftClick = None,
        onMenuResolve = None,
        onHovering = None,
        imagePath = None,
        audioPath = None
    ):

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            onLeftClick = onLeftClick,
            onMenuResolve = onMenuResolve,
            onHovering = onHovering,
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            padding = padding,
            imagePath = imagePath,
            audioPath = audioPath
        )

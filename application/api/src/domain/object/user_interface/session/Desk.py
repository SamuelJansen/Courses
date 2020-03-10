import Modal, Button
import surfaceFunction, itemSetFunction

print('Desk library imported')

class Desk(Modal.Modal):

    def __init__(self,name,size,itemsPerLine,father,
        position = None,
        text = None,
        textPosition = None,
        fontSize = None,
        scale = None,
        padding = None,
        noImage = False,
        onLeftClick = None,
        onMenuResolve = None,
        imagePath = None,
        audioPath = None
    ):

        deskPaddingInConstructionTime = None

        Modal.Modal.__init__(
            self,name,size,father,
            position = position,
            onLeftClick = onLeftClick,
            onMenuResolve = onMenuResolve,
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = scale,
            padding = deskPaddingInConstructionTime,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = imagePath
        )

        self.itemsPerLine = self.size[0] // 80
        self.padding = padding

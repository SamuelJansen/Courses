import Modal, Button
import surfaceFunction, itemSetFunction

print('Desk library imported')

class Desk(Modal.Modal):

    def __init__(self,name,size,itemsPerLine,father,
        position = None,
        externalFunction = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        audioPath = None
    ):

        deskPaddingInConstructionTime = None

        Modal.Modal.__init__(
            self,name,size,father,
            position = position,
            externalFunction = externalFunction,
            scale = scale,
            padding = deskPaddingInConstructionTime,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = imagePath
        )

        self.itemsPerLine = self.size[0] // 80
        self.padding = padding

        print(f'Desk.name = {self.name}, Desk.userInterfaceSurface.name = {self.userInterfaceSurface.name}, Desk.userInterfaceSurface.padding = {self.userInterfaceSurface.padding}')

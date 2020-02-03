import Surface

print('Modal library imported')

class Modal(Surface.Surface):
    def __init__(self,name,position,size,father,
        functionKey = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        father, padding = self.setModelAsFloorChild(father,padding)

        Surface.Surface.__init__(
            self,name,position,size,father,
            functionKey = functionKey,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.setModelBackOnTop()

    def setModelAsFloorChild(self,father,padding):
        self.modalFather = father
        father = self.modalFather.application.getFloor()
        if not padding :
            padding = self.modalFather.userInterfaceSurface.padding

        return father, padding

    def setModelBackOnTop(self):
        self.blitOrder = self.modalFather.blitOrder + 1
        print(f'newBlitOrder = {self.blitOrder}')
        self.userInterfaceSurface = self.modalFather.userInterfaceSurface
        self.screen.surface.blit(self.modalFather.image,[0,0])
        self.handler.updateOriginalAttributes()

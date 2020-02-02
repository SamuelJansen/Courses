import Surface

print('Modal library imported')

class Modal(Surface.Surface):
    def __init__(self,name,position,size,father,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        self.modalFather = father
        father = self.modalFather.aplication.getFloor()

        Surface.Surface.__init__(
            self,
            name,
            position,
            size,
            father,
            scale = scale,
            padding = self.modalFather.padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.blitOrder = self.modalFather.blitOrder + 1
        print(f'newBlitOrder = {self.blitOrder}')
        self.userInterfaceSurface = self.modalFather.userInterfaceSurface
        self.screen.surface.blit(self.modalFather.image,[0,0])
        self.handler.updateOriginalAttributes()

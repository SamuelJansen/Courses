from model.object.user_interface import UserInterfaceSurface
from model.object import Object

class Modal(UserInterfaceSurface.UserInterfaceSurface):
    def __init__(self,name,position,size,father,
        scale = None,
        padding = [0,0],
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        self.modalFather = father
        father = father.aplication.getFloor()

        UserInterfaceSurface.UserInterfaceSurface.__init__(
            self,
            name,
            position,
            size,
            father,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        # if self.modalFather :
        self.blitOrder = self.modalFather.blitOrder + 1
        print(f'newBlitOrder = {self.blitOrder}')
        self.screen.surface.blit(self.modalFather.image,[0,0])
        self.handler.updateOriginalAttributes()

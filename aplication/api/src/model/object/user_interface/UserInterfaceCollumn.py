from model.object.user_interface import UserInterface, UserInterfaceSurface, Button

class UserInterfaceCollumn(UserInterfaceSurface.UserInterfaceSurface):
    def __init__(self,name,position,size,father,
        scale = None,
        padding = [0,0],
        imagePath = None,
        soundPath = None
    ):

        UserInterfaceSurface.UserInterfaceSurface.__init__(
            self,
            name,
            position,
            size,
            father,
            scale = scale,
            padding = padding,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.previousChildrenPosition = [0,0]

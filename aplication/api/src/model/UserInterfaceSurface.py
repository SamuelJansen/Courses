from model import UserInterface

class UserInterfaceSurface(UserInterface.UserInterface):

    def __init__(self,name,position,size,scale,father,
        imagePath = None,
        soundPath = None
    ):

        UserInterface.UserInterface.__init__(
            self,name,position,size,scale,father,
            imagePath = imagePath,
            soundPath = soundPath
        )

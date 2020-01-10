from model import UserInterface

class UserInterfaceSurface(UserInterface.UserInterface):

    def __init__(self,name,position,size,scale,father,aplication,
        imagePath = None,
        soundPath = None
    ):

        UserInterface.UserInterface.__init__(
            self,name,position,size,scale,father,aplication,
            imagePath = imagePath,
            soundPath = soundPath
        )

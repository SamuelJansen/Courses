from model.object.user_interface import UserInterface, Button

print('UserInterfaceSurface library imported')

class UserInterfaceSurface(UserInterface.UserInterface):

    def __init__(self,name,position,size,scale,father,
        padding = [0,0],
        imagePath = None,
        soundPath = None
    ):

        self.userInterfaceSurface = self

        UserInterface.UserInterface.__init__(
            self,name,position,size,scale,father,
            padding = padding,
            imagePath = imagePath,
            soundPath = soundPath
        )

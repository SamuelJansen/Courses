import UserInterface

print('Button library imported')

class Button(UserInterface.UserInterface):

    def __init__(
        self,name,position,size,father,
        functionKey = None,
        padding = None,
        imagePath = None,
        soundPath = None
    ):

        if not imagePath :
            imagePath = f'{father.application.pathMannanger.getApiModulePath(father.application.name)}resourse\\button\\image\\'
        if not soundPath :
            soundPath = f'{father.application.pathMannanger.getApiModulePath(father.application.name)}resourse\\button\\sound\\'

        UserInterface.UserInterface.__init__(
            self,name,position,size,father,
            functionKey = functionKey,
            padding = padding,
            imagePath = imagePath,
            soundPath = soundPath
        )

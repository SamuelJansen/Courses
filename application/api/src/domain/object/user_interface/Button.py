import UserInterface

print('Button library imported')

class Button(UserInterface.UserInterface):

    def __init__(
        self,name,position,size,father,
        externalFunction = None,
        padding = None,
        imagePath = None,
        audioPath = None
    ):

        if not imagePath :
            imagePath = f'{father.application.pathMannanger.getApiModulePath(father.application.name)}resourse\\button\\image\\'
        if not audioPath :
            audioPath = f'{father.application.pathMannanger.getApiModulePath(father.application.name)}resourse\\button\\audio\\'

        UserInterface.UserInterface.__init__(
            self,name,position,size,father,
            externalFunction = externalFunction,
            padding = padding,
            imagePath = imagePath,
            audioPath = audioPath
        )

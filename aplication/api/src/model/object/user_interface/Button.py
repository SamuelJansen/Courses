print('Button library imported')

from model.object.user_interface import UserInterface
from function.eventFunction import eventFunctions, getFunctionKey

class Button(UserInterface.UserInterface):

    def __init__(
        self,name,position,size,functionKey,father,
        padding = None,
        scale = None,
        imagePath = None,
        soundPath = None
    ):

        if not imagePath :
            imagePath = f'{father.aplication.pathMannanger.getApiModulePath(father.aplication.name)}resourse\\button\\image\\'
            print(f'imagePath = {imagePath}')
        if not soundPath :
            soundPath = f'{father.aplication.pathMannanger.getApiModulePath(father.aplication.name)}resourse\\button\\sound\\'

        UserInterface.UserInterface.__init__(
            self,name,position,size,scale,father,
            imagePath = imagePath,
            soundPath = soundPath
        )

        self.functionKey = getFunctionKey(functionKey)
        self.run = eventFunctions[self.functionKey]

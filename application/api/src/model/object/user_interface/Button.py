import UserInterface

import eventFunction # eventFunctions, getFunctionKey

print('Button library imported')

class Button(UserInterface.UserInterface):

    def __init__(
        self,name,position,size,functionKey,father,
        padding = None,
        imagePath = None,
        soundPath = None
    ):

        print(f'                        Button.size = {size}')

        if not imagePath :
            imagePath = f'{father.aplication.pathMannanger.getApiModulePath(father.aplication.name)}resourse\\button\\image\\'
            print(f'imagePath = {imagePath}')
        if not soundPath :
            soundPath = f'{father.aplication.pathMannanger.getApiModulePath(father.aplication.name)}resourse\\button\\sound\\'

        UserInterface.UserInterface.__init__(
            self,name,position,size,father,
            padding = padding,
            imagePath = imagePath,
            soundPath = soundPath
        )

        self.functionKey = eventFunction.getFunctionKey(functionKey)
        self.run = eventFunction.eventFunctions[self.functionKey]
